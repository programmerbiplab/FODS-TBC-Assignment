'''The following program is a guessing game where
user keeps guessing the computer generated number for a maximum of
5 times until the guessed number is correct'''

import random

#Generates a random number within a fixed range
answer = random.randint(1, 100)

#Giving user 5 guesses
for attempt in range(1, 6):
    #For counting the attempts
    
    user_input = input(f"Attempt {attempt}/5 - Guess the number: ")

    # Validation if the input is a number or not
    if not user_input.isdigit():
        print("Invalid input! Please enter a valid number.")
        continue

    guess = int(user_input)

    # Feedback by machine for correctness of guesses by the uses
    if guess < answer:
        print("Too low.")
    elif guess > answer:
        print("Too high.")
    else:
        #Correct guess message
        print("Correct number. Good guess!!")
        break
else:
    # Message after unsuccessful attempt at guessing the number
    print("Game Over. The correct number was:", answer)

#by Biplab Prasad Gajurel 25024641