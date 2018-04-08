#! /usr/bin/env python3
import sys, math

#read in M the number of numbers
M = int(sys.stdin.readline())

#read in the next M numbers in in the format ## or #^#^#...
numbers = []
comparisons = []
powernumbers = []
for i in range(M):
    numbers.append(sys.stdin.readline().strip())
print(numbers)

#figure out what numbers need to be converted to ints from format #^#...
for val in numbers:
    if '^' in val:
        powernumbers.append(val)
    else:
        comparisons.append(int(val))
print(powernumbers)
print(comparisons)


#FUNCTION TO COMPARE EXPONENT numbers
def expcompare(one, two):
    tempmax = 0
    templena = len(one)
    templenb = len(two)
    if templena > templenb:
        maxtemplen = templena
    else:
        maxtemplen = templenb

    for i in range(0,maxtemplen,2):
        if int(one[i]) == int(two[i]):
            if int(one[i+2]) > int(two[i+2]):
                tempmax = one
            else:
                tempmax = two
        if int(one[i]) > int(two[i]):
            if math.pow(int(one[i]), int(one[i+2])) > math.pow(int(two[i]), int(two[i+2])):
                tempmax = one
            else:
                tempmax = two
        if int(one[i]) < int(two[i]):
            tempmax = two
    return tempmax


print("EXPCOMPARE: ", expcompare(powernumbers[0], powernumbers[1]))

#for num in powernumbers:
#    length = len(num)
#    if len == 3:
#        comparisons.append(math.pow(int(num[0]),int(num[2]))
#    else:


'''
temp = []
length = 0
_temp = 0

for num in powernumbers:
    for index in num:
        if index.isdigit():
            temp.append(index)
        length = len(temp)
    if length > 0:
        for j in reversed(range(len(temp)-1)):
            if _temp == 0:
                print("   j-1 =", temp[j-1])
                print("   j =", temp[j])
                _temp = int(math.pow(int(temp[j]), int(temp[j-1]))) #only works for len 2
            else:
                print("   j-1 =", temp[j-1])
                _temp = int(math.pow(int(temp[j-1]), _temp))
        numbervals.append(_temp)
        _temp = 0

print("_TEMP:", _temp)
print("POWERNUMBERS:", powernumbers)
print("NUMBERVALS:", numbervals)
print("NUMBERS:", numbers)
'''
