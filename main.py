# Number Guessing Game that tells User lower or higher

# Import random module
import random

run = True

answer = int(random.randint(1, 101))

while run:

    guess = int(input("Guess a number between 1 - 100: "))

    if guess == answer:
        print(f"{answer} is correct! YOU WIN!")
        break
    elif guess > answer:
        print(f"{guess} is too big!")
    elif guess < answer:
        print(f"{guess} is too small")
    else:
        print("Please guess between 1 - 100")