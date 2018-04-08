#! /usr/bin/env python3
import sys

answers = []
badpairs = []
n = []
m = []
temp = []

while temp != ['0', '0']:
    temp = sys.stdin.readline().split()
    N = int(temp[0])
    M = int(temp[1])
    if N != 0 and M != 0:
        n.append(N)
    if M != 0:
        m.append(M)

    if M == 0 and N != 0:
        answers.append(1)
        continue
    else:
        for i in range(M):
            badpairs.append(sys.stdin.readline().strip().split())
        continue

print("n =", n)
print("m =", m)
print("BADPAIRS:", badpairs)
print("ANS:", answers)


for index in m:
    int(index)
    for pairs in range(index):
        print("PAIRS:", pairs)


print("CASEPAIRS:", casepairs)
