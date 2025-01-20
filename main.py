# Number Guessing Game that tells User lower or higher

# Import random module
import random

# Run the program and set guesses to 0
run = True
guesses = 0

answer = int(random.randint(1, 101))   # Set random int as answer

# Main game loop
while run:

    guess = input("Guess a number between 1 - 100: ")   # Prompt user input

# Use a try / except statement to catch Value Errors
    try:
        guess = int(guess)   # Turn User input into int
        if guess == answer:   # Print Win message
            print(f"{answer} is correct! YOU WIN!")
            print(f"Number of guesses: {guesses}")
            break
        elif guess > answer:  # If guess is bigger than answer
            print(f"{guess} is too big!")
            guesses += 1      # Add +1 to guesses
        elif guess < answer:  # If guess is bigger than answer
            print(f"{guess} is too small")
            guesses += 1      # Add +1 to guesses
        else:
            print("Please guess between 1 - 100")  # Catches error if number isn't in range

    except ValueError:
        print("Invalid Input. Please enter a number 1 - 100.")