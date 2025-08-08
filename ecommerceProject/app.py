from flask import Flask, render_template, request
from sentence_transformers import SentenceTransformer, util
import json
import os

app = Flask(__name__)

# Load the sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load product data from JSON file
with open(os.path.join(app.root_path, 'products.json'), 'r') as f:
    products = json.load(f)

# Precompute embeddings for all product descriptions
for product in products:
    text = f"{product['name']} {product['description']} {product['category']}"
    product['embedding'] = model.encode(text, convert_to_tensor=True)


def parse_query(query):
    parsed = {
        "category": None,
        "max_price": None,
        "min_price": None,
        "keywords": []
    }

    if not query:
        return parsed

    words = query.lower().split()

    # Detect category from query
    known_categories = list(set([p['category'].lower() for p in products]))
    for word in words:
        if word in known_categories:
            parsed['category'] = word
            break

    # Detect price constraints from query
    for i, word in enumerate(words):
        if word in ['below', 'under', '<']:
            try:
                value = words[i + 1].replace('$', '')
                parsed['max_price'] = float(value)
            except:
                continue
        elif word in ['above', 'over', '>', 'more', 'greater']:
            try:
                value = words[i + 1].replace('$', '')
                parsed['min_price'] = float(value)
            except:
                continue

    # Exclude common filter words and digits from keywords
    skip_words = ['below', 'under', 'over', 'above', '<', '>', 'more', 'greater', 'than', 'for', 'price', 'cost', '$']
    parsed['keywords'] = [w for w in words if w not in skip_words and not w.replace('$', '').isdigit()]

    return parsed


@app.route('/')
def index():
    query = request.args.get('query', '').strip()
    category_input = request.args.get('category', '').strip().lower()
    filtered = products

    if not query and not category_input:
        return render_template('index.html', products=products)

    parsed = parse_query(query)

    # Apply category filter: dropdown has priority over query category
    if category_input:
        filtered = [p for p in filtered if category_input in p['category'].lower()]
    elif parsed['category']:
        filtered = [p for p in filtered if parsed['category'] in p['category'].lower()]

    # Apply price filters from query parsing
    if parsed['max_price'] is not None:
        filtered = [p for p in filtered if p.get('price', float('inf')) <= parsed['max_price']]
    if parsed['min_price'] is not None:
        filtered = [p for p in filtered if p.get('price', 0) >= parsed['min_price']]

    # Semantic similarity search within the filtered products
    if query:
        query_embedding = model.encode(query, convert_to_tensor=True)
        scored = []
        for product in filtered:
            score = util.cos_sim(query_embedding, product['embedding']).item()
            scored.append((score, product))
        # Sort by descending similarity score
        scored.sort(reverse=True, key=lambda x: x[0])
        filtered = [p for _, p in scored]

        # Additional keyword filtering (strict) on the final list
        if parsed['keywords']:
            keywords = parsed['keywords']
            filtered = [
                p for p in filtered
                if any(k in f"{p['name']} {p['description']} {p['category']}".lower() for k in keywords)
            ]

    return render_template('index.html', products=filtered)


if __name__ == '__main__':
    app.run(debug=True)


"""
--- DEVELOPMENT HISTORY & ATTEMPTS ---

# Attempt 1: Simple keyword and category filtering without semantic search
# This was too basic and returned many irrelevant results.
'''
if query:
    filtered = [p for p in filtered if query in p['name'].lower() or query in p['description'].lower()]
if category:
    filtered = [p for p in filtered if category in p['category'].lower()]
'''

# Attempt 2: Semantic search on entire products list ignoring price filters first
# Issue: When price filter applied after semantic search, some products wrongly excluded.
'''
query_embedding = model.encode(query, convert_to_tensor=True)
scored = []
for product in products:
    score = util.cos_sim(query_embedding, product['embedding']).item()
    scored.append((score, product))
scored.sort(reverse=True, key=lambda x: x[0])
filtered = [p for score, p in scored if score > 0.3]

if category:
    filtered = [p for p in filtered if category in p['category'].lower()]
if max_price:
    filtered = [p for p in filtered if p['price'] <= max_price]
'''

# Attempt 3: Filtering first by category and price, then semantic search on filtered results
# This approach worked best and improved relevance and filtering accuracy.
# We kept keywords filter on top of semantic similarity to improve strictness.

# Attempt 4: Tried applying similarity threshold >0.3 to remove low similarity products
# Problem: Sometimes relevant products fell below threshold and were missed.
# So, we removed the threshold and rely on keyword filtering after semantic sort.

# Attempt 5: Tried to boost semantic scores for products matching keywords for sorting
# Caused irrelevant results to appear at top (e.g. mouse for backpack queries)
# Removed boosting for cleaner relevance sorting.

# Notes:
# - Parsing price constraints carefully to handle 'under', 'below', 'above', 'over', etc.
# - Keywords filtered to avoid stop words and numeric tokens.
# - Category filter from dropdown takes precedence over parsed category from query.
"""
