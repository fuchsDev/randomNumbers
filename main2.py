#imports
from random import randint

#menu
print("\n******************* Python Dice Simulator *******************")
print("\nDo you want to throw the dice? (y / n)")
choiceUser = str(input("Enter y for Yes or n for No: "))

#loop
while (choiceUser != 'n'):
    if choiceUser == 'y':
        dice = randint(1,6)
        print("You chose to roll the dice, and the number generated was:")
        print(dice)
        choiceUser = str(input("Do you want to continue?(y/n)"))
    else:
        print("Invalid Option")
        break 