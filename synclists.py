#! usr/bin/env Python3
while True:
    n = int(input())
    if n != 0:
        listOne, listTwo = [], []
        for i in range(n): listOne.append(int(input()))
        for i in range(n): listTwo.append(int(input()))
        print("listOne: ", listOne)
        print("listTwo: ", listTwo)
        #ALGO options:
        #   find the rankings of listOne and listTwo
        #   apply the rankings order of ListOne
        #    to the contents of listTwo
        for item in listOne:

    else: break
