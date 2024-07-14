import art
import random
print(art.logo)


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Takes the list of cards and calculates the score"""
    # checks if its blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    # checks for ace, and replaces it with 1 if value is over 21
    elif sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You lose! The opponent has BlackJack!"
    elif user_score == 0:
        return "You Win!! Its a BlackJack!"
    elif user_score > 21:
        return "You went over! You Lose!"
    elif computer_score > 21:
        return "The opponent went over, You Win!!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    # gets 2 cards randomly for each
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, and your score: {user_score}")
        print(f"The computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to stand: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand is: {user_cards} and you final score is: {user_score}")
    print(f"The opponent's final hand is: {computer_cards}, and the final score is: {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play BlackJack? Type 'yes' or 'no'.").lower() == "y":
    play_game()
n