# Make a number guessing game.
# User inputs a number until they get it right.
# Hidden number is randomly generated.
# input() -> int()

import random

number = random.randint(-100, 100)

user_input = input(f"Guess the number: ")
while user_input != number:
    user_input = int(user_input)

    if user_input == number:
        print("correct!")
        number = random.randint(-100, 100)
    elif user_input < number:
        print("Too low")
    elif user_input > number:
        print("Too high")

    user_input = input(f"Guess the number: ")
