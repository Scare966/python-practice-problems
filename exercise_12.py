# Write a program that takes a list of numbers and makes a new list of only the first and last elements of the given list.

import random

def listpos():
    random_list = []
    for i in range(0,5):
        n = random.randint(0,15)
        
        random_list.append(n[0])
        random_list.append(n[-1])
    
    print(random_list)


