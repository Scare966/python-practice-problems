def divisor():
    divNum = int(input("What is your number: "))
    
    listRange = list(range(1, divNum+1))

    divList = []

    for num in listRange:
        if divNum % num == 0:
            divList.append(num)
    
    print(divList)

divisor()