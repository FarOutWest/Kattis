#! /usr/bin/env python3
import sys

#read in the first line as the string to manipulate 1 <= stringlen <= 1 000 000
#read in the second line as the sequence of explosion based string 1 <= stringlen <= 36
string = sys.stdin.readline().strip()
exp = sys.stdin.readline().strip()
print("LEN STRING: ", len(string))
print("LEN EXP: ", len(exp))

#search through the first string looking for the second as a substring
#if found remove substring from string and repeate
#else return first string (with manipulations)
#while exp in string:
#    string = string.replace(exp, '')

possibles = []
for i, char in enumerate(string):
    print("i = ", i)
    print("char = ", char)
    if char == exp[0]:
        possibles.append(i)
#possibles = [i for char in enumerate(string) if char == exp[0]]
print("POSSIBLES: ", possibles)

remove = ''
for count in range(len(possibles)-1):
    for i in range(possibles[count], possibles[count]+len(exp)):
        remove = remove + string[i]
        print("REMOVE: ", remove)
        if remove == exp:
            string = string.replace(remove, '')
            print("STRING: ", string)
            remove = ''

#if returned string is NULL print "FRULA" else print returned string
if string == '':
    print('FRULA')
else:
    print(string)
