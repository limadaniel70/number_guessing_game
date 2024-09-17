import random

from numpy import diff

print(
    """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have 5 chances to guess the correct number.\n"""
)

difficulties = {
    1: {"level": "Easy", "chances": 10},
    2: {"level": "Medium", "chances": 5},
    3: {"level": "Hard", "chances": 3},
}

print(
    """Select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""
)

difficulty = int(input("Enter your choice: "))
if difficulty < 1 or difficulty > 3:
    raise Exception("Invalid number")

print(
    f"""Great! You have selected the {difficulties[difficulty]["level"]} difficulty level.
Let's start the game!\n"""
)

number = random.randint(1, 100)

attempt = 0

while attempt <= difficulties[difficulty]["chances"]:
    guess = int(input("Enter your guess: "))
    attempt += 1
    if guess > number:
        print(f"Incorrect! The number is less than {guess}.\n")
        continue
    elif guess < number:
        print(f"Incorrect! The number is greater than {guess}.\n")
        continue
    elif guess == number:
        print(f"Congratulations! You guessed the correct number in {attempt} attempts.\n")
        break