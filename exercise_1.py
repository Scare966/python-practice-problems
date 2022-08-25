#name, age, when they will turn 100 years old

def yearsold():
    name = input("What is your name: ")
    age = int(input("What is your age: "))
    year = 2022 - age + 100

    print(year)

yearsold()

