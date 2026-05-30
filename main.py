#When the game starts, it should display a welcome message along with the rules of the game.
#The computer should randomly select a number between 1 and 100.
#User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess the number.
#The user should be able to enter their guess.
#If the user's guess is correct, the game should display a congratulatory message along with the number of attempts it took to guess the number.
#If the user's guess is incorrect, the game should display a message indicating whether the number is greater or less than the user's guess.
#The game should end when the user guesses the correct number or runs out of chances.

import random
import sys

def main():
    print("Welcome to the Number Guessing Game!")
    print("What difficulty do you want?" )
    print("1. Easy = 10 chances.")
    print("2. Medium = 5 chances.")
    print("3. Hard = 3 chances.")

    choice = input("1, 2 or 3? " )
    chances = None

    if choice == "1":
        chances = 10
        valid = True
    elif choice == "2":
        chances = 5
        valid = True
    elif choice == "3":
        chances = 3
        valid = True
    else:
        valid = False

    return [valid, chances]

def check(num, choice):
    if num > choice:
        print("Your guess is less than the computers number!")
        return True
    elif num <  choice:
        print("Your guess is higher than the computers number!")
        return True
    elif num == choice:
        print("You win well done!")
        sys.exit()
    else:
        print("Invalid number!")
        return False

def game(settings):
    global loop
    valid = settings[0]
    chances = settings[1]
    num = random.randint(1, 100)

    while chances > 0:
        if valid == True:
            chances -= 1
            choice = int(input("What is your guess? " ))
            valid  = check(num, choice)
        else:
            return
        
    print("You ran out of chances!")
    chances = 0
    sys.exit()

        

loop =  True
while loop:
    settings = main()
    if settings[0] == True:
        game(settings)
    else:
        print("Invalid Input!")
        continue