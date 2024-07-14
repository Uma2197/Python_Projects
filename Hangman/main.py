import hangman_words
import hangman_art
import random
print(hangman_art.logo)
word_list = hangman_words.word_list
# Randomly pick a word from the list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
# Test code
# print(f"The word is {chosen_word}")
# Creating an empty list [_, _, _]
display = []
for _ in chosen_word:
    display += "_"
print(display)

# Get an input from the user
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    # Check if the letter is one of the letters of the chosen word, if guessed right, replace the
    # _ to guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
    # Replacing _ by the guessed letter if guessed right.
        if letter == guess:
            display[position] = letter
    print(display)
    if guess not in chosen_word:
        print("The letter is not in the word, make another guess")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You lost all the lives, you lose!")

    if "_" not in display:
        end_of_game = True
        print("That's great! You Win!!")
    # printing the diagram
