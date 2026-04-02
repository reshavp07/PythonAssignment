# Develop a game where the computer picks a random number between 1 and 10, and the user attempts to guess it. After each guess, the program provides feedback: Too high, Too low, or Correct. The number remains the same throughout the game until the user guesses correctly.
# The computer picks a secret number between 1 and 10
# We use a loop to keep the game going until the guess is correct
# We will ask the user for their guess

import random


secret_number = random.randint(1, 10)

print("I'm thinking of a number between 1 and 10. Can you guess it?")


while True:

    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Correct! You nailed it.")
        break