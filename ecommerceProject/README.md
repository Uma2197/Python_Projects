# Ecommerce Product Search with Semantic NLP and Flask

This project is a Flask web application that enables smart product searching with natural language queries using semantic similarity. It leverages the `sentence-transformers` library to encode product information and user queries, allowing fuzzy and meaningful search beyond exact keyword matching.

---

## Features

- Semantic search on product name, description, and category using Sentence Transformers (`all-MiniLM-L6-v2`)
- Parsing of natural language queries to detect:
  - Category filters (e.g., "electronics", "clothing")
  - Price constraints (e.g., "under $60", "above 100")
  - Keyword matching for more precise filtering
- Combined use of dropdown category filter and free-text search
- Filtering and ranking of products based on semantic similarity scores
- Clean, simple Flask web interface for product listing and search

---

## Setup Instructions

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Install dependencies

```bash
pip install flask sentence-transformers torch
```

### Prepare product data

Add your product data to `products.json` file in the project root.

Each product should have at least: `name`, `description`, `category`, and `price` fields.

Example entry:

```json
{
  "name": "Running Shoes",
  "description": "Comfortable running shoes for everyday use.",
  "category": "Footwear",
  "price": 75.0
}
```

---

## Run the application

From the project root directory, run:

```bash
python app.py
```

Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the app.

---

## Usage

- Use the search box to enter natural language queries like:
  - "show me running shoes under 80"
  - "electronics above 60"
  - "backpack for everyday use"
- Optionally, select a category from the dropdown to filter results further.

The results are ranked by semantic similarity and filtered by category and price constraints.

---

## Project Structure

```
/ecommerceProject
  ├── app.py             # Flask application with semantic search
  ├── products.json      # Product data file
  ├── templates/
      └── index.html     # HTML template for product display and search form
  └── README.md          # This README file
```

---

## GitHub Repository

You can find this project on my GitHub at:

[https://github.com/Uma2197/Python_Projects/tree/main/ecommerceProject](https://github.com/Uma2197/Python_Projects/tree/main/ecommerceProject)

---

## Notes

- The project uses the `all-MiniLM-L6-v2` sentence transformer model for efficient semantic encoding.
- Precomputing embeddings for products improves performance.
- Price parsing handles terms like "under", "below", "above", and "over" with numeric values.
- The semantic similarity threshold and filtering can be adjusted in the code for different behavior.

---

## License

This project is open source and available under the MIT License.

---

## Contact

If you have questions or suggestions, feel free to reach out!

---

Thank you for checking out this project!
