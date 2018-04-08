#! usr/bin/env Python3

import sys

X = sys.stdin.readline().strip()
N = sys.stdin.readline().strip()
Pi = []

for i in range(int(N)):
    Pi.append(sys.stdin.readline().strip())

Pi = [int(X) - int(i) for i in Pi]
out = int(X) + sum(Pi)
print(out)
