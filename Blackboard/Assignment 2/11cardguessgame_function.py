'''The following program takes user input of card guessing game and
guesses the user input with computer generated one for value of the card and
the suit of the card and displays if the guessed card is correct and
shows a message if the guess is wrong'''

import random

# Defining card properties, suit abd value
card_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
card_suits = ['heart', 'diamond', 'club', 'spades']

# Making the computer randomly select a card
answer_value = random.choice(card_values)
answer_suit = random.choice(card_suits)

# Stores computer's answer in a list
answer = [answer_value, answer_suit]

# Asking for player to guess
print("Welcome to the Card Guessing Game!")
print("Guess the card!")

player_value = input("Enter card value (e.g. 2, 3, ... Jack, Queen, King, Ace): ").strip()
player_suit = input("Enter card suit (heart, diamond, club, spades): ").strip()

# To compute the guess of user and computer
value_correct = (player_value.lower() == answer_value.lower())
suit_correct = (player_suit.lower() == answer_suit.lower())

print("\n--- Result ---")

if value_correct and suit_correct:
    print("Congratulations! You guessed both value and suit correctly. You're a genius")
elif value_correct or suit_correct:
    print("Good try! Only one part was correcttly guessed!")
    print("Answer was:", answer_value, "of", answer_suit)
else:
    print("Game Over! Both guesses were wrong.Better luck next time.")
    print("Answer was:", answer_value, "of", answer_suit)

# By Biplab Prasad Gajurel 25024641