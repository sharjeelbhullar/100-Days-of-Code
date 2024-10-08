print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`." / ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input("Enter your choice left or right: ")
lChoice1 = choice1.lower()
if lChoice1 == "left":
    choice2 = input("Do you want to swim or wait? ")
    lChoice2 = choice2.lower()
    if lChoice2 == "wait":
        choice3 = input("Please select your favourite color options are: Blue, Red and Yellow ")
        lChoice3 = choice3.lower()
        if lChoice3 == "yellow":
            print("You win!")
        elif lChoice3 == "blue" or lChoice3 == "red":
            print("Game Over.")
        else:
            print("Please enter a valid choice or check your spelling.")
    elif lChoice2 == "swim":
        print("Game Over.")
    else:
        print("Please enter a valid choice or check your spelling.")
elif lChoice1 == "right":
    print("Game Over.")
else:
    print("PLease enter a valid choice or check your spelling.")


