#! usr/bin/env Python3
import sys
N = int(sys.stdin.readline().strip())
a = []
for i in range(N):
    a.append(int(sys.stdin.readline().strip()))
for i in a:
    if i % 2 == 0: print(i, " is even")
    else: print(i, " is odd")
