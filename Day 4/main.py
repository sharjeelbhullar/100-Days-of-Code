print("Welcome to the \"Rock Scissor Paper\" Game.")
import  random
rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("You entered invalid number. Please enter numbers from 0, 1 and 2.")
    exit()


computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choice == computer:
    print("It's a draw.")
elif choice == 0 and computer == 2:

    print("You win")
elif choice == 2 and computer == 1:

    print("You win")
elif choice == 1 and computer == 0:
    print("You win")
else:
    print("You lose")