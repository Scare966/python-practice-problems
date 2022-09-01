# Ask the user for a number and determine whether the number is prime or not.

# method one, using more steps

def primeNum():
    number = int(input("What is your number: "))

    if number % 2 == 0:
        print("This is an even number, try again.")
        return number
    else:
        print("This is a prime number.") 
primeNum()

# method two practicing with return statements

def get_prime(numbers):
    return [num for num in numbers if num % 2]
print(get_prime([1,2,3,4,5,6]))