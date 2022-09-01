# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random

def guessgame():
    a = random.randint(1, 9)
    b = int(input("What is your guess, any number 1 - 9: "))

    if b == a:
        print("You guessed correctly!")
    elif b > a:
        print("You guessed too high!")
    elif b < a:
        print("You guessed too low!")
    else:
        print("Your guess was outside the range, try again.")

guessgame()