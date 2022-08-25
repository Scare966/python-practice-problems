#odd or even

from ast import Num


def oddeven():
    given = int(input("What is your number: "))

    if given % 2 == 0:
        print("Your number is even...")
    
    elif given % 2 != 0:
        print("Your number is odd...")

oddeven()
