import random
import art
print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
decided_number = random.randint(1,100)
print(f"Decided number is: {decided_number}")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    moves = 10
    while moves != 0:
        for i in range(10):
            print(f"You have {moves} attempts remaining to guess the number.")
            guess = int(input("Make a guess: "))
            if guess == decided_number:
                print(f"You got it! The answer was {decided_number}")
                break
            elif guess > decided_number:
                print("Too high.")
                moves -= 1
            elif guess < decided_number:
                print("Too low")
                moves -= 1
            else:
                print("Something went wrong.")
    if moves == 0:
        print("You've run out of guesses, you lose.")

elif level == "hard":
    moves = 5
    while moves != 0:
        print(f"You have {moves} attempts remaining to guess the number.")
        for i in range(5):
            guess = int(input("Make a guess: "))
            if guess == decided_number:
                print(f"You got it! The answer was {decided_number}")
                break
            elif guess > decided_number:
                print("Too high.")
                moves -= 1
            elif guess < decided_number:
                print("Too low")
                moves -= 1
            else:
                print("Something went wrong.")
    if moves == 0:
        print("You've run out of guesses, you lose.")
