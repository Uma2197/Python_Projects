import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

alphabet_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict = {row.letter: row.code for (index, row) in alphabet_data_frame.iterrows()}
print(new_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# Exception handling with while loop, My solution:
# is_done = False
# while not is_done:
#     user_word = input("Enter a word:").upper()
#     try:
#         phonetic_code_words = [new_dict[letter] for letter in user_word]
#     except KeyError:
#         print("Sorry, only letters from the alphabets please")
#     else:
#         print(phonetic_code_words)
#         is_done = True


# Exception handling with function call:, Angela's solution:
def generate_phonetics():
    user_word = input("Enter a word:").upper()
    try:
        phonetic_code_words = [new_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry, only letters from the alphabets please")
        generate_phonetics()
    else:
        print(phonetic_code_words)


generate_phonetics()