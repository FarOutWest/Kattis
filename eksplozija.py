#! /usr/bin/env python3
import sys
import re

#read in the first line as the string to manipulate 1 <= stringlen <= 1 000 000
#read in the second line as the sequence of explosion based string 1 <= stringlen <= 36
string = sys.stdin.readline().strip()
exp = sys.stdin.readline().strip()

#check that the length of strings are valid
#if len(string) < 1 or len(string) > 1000000:
    #exit()
#if len(exp) < 1 or len(exp) > 36:
    #exit()

#search through the first string looking for the second as a substring
#if found remove substring from string and repeate
#else return first string (with manipulations)
while exp in string:
    string = re.sub(exp, '', string)

#while exp in string:
    #string = string.replace(exp, '')

#if returned string is NULL print "FRULA"
#else print returned string
if string == '':
    print('FRULA')
else:
    print(string)
