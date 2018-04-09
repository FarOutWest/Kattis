#! usr/bin/env Python3
import sys
trips = []
ans = []
T = int(sys.stdin.readline().strip())
for i in range(T):
    n = int(sys.stdin.readline().strip())
    for j in range(n):
        trips.append(sys.stdin.readline().strip())
    trips = list(set(trips))
    ans.append(len(trips))
    trips = []
for i in ans: print(i)
