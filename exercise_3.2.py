# Ask the user for a number and return a list that contains only elements from the original list 'a' that are smaller than that number given by the user.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
given = int(input("What is your number: "))
lessThan = []

for num in numbers:
    if num < given:
        lessThan.append(num)

print(lessThan)

