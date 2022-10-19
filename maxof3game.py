## game where you take 3 input variables and return largest using max() function

def maxof3():
    x, y, z = input("Enter 3 numbers, no commas: ").split()
    a = max(x, y, z)
    print(a)
    
maxof3()

