#! /usr/bin/env python3
import sys

#read in N the number of test cases
N = int(sys.stdin.readline())

#read in the next N lines as the test cases they are one line each containing P and the string
data = []
for i in range(N):
    data.append(sys.stdin.readline().strip().split())

print(data)

p = []
messages = []
for index in data:
    p.append(index[0])
    messages.append(index[1])

print(p)
print(messages)

#loop through the test cases and determing the original message as integers
for val in p:
    
