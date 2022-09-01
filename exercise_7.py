# write one line of python that takes a list and makes a new list with only the even elements in it

def listEven():
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [element for element in a if element % 2 == 0]

    print(b)

listEven()

