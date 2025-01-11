# Number Guessing Game that tells User lower or higher

# Import random module
import random

run = True
guesses = 0

answer = int(random.randint(1, 101))

while run:

    guess = input("Guess a number between 1 - 100: ")

    try:
        guess = int(guess)
        if guess == answer:
            print(f"{answer} is correct! YOU WIN!")
            print(f"Number of guesses: {guesses}")
            break
        elif guess > answer:
            print(f"{guess} is too big!")
            guesses += 1
        elif guess < answer:
            print(f"{guess} is too small")
            guesses += 1
        else:
            print("Please guess between 1 - 100")

    except ValueError:
        print("Invalid Input. Please enter a number 1 - 100.")