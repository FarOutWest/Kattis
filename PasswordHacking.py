#! /usr/bin/env python3
import sys

#input number of passwords as a line as N
#read in the next N passwords and their probability
N = sys.stdin.readline().strip().split()
for i in N:
    N = int(i)

passandprobs = []
for x in range(0, N):
    passandprobs.append(sys.stdin.readline().strip().split())

print(passandprobs)

#verify that len(passwords) > 0 and <=12
#verify that probabilities have #.#### decimal values & all add up to 1


#Assume 500 passwords in list and total probabilities = 1

#Output on a single line the expected number of attempts to find the correct passwords
#Answers within 10^-4 of the correct answer will be accepted
