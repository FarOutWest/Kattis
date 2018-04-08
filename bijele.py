#! usr/bin/env Python3
import sys
p = sys.stdin.readline().split()
p = [int(i) for i in p]
actual = [1, 1, 2, 2, 2, 8]
ans = [a-b for a,b in zip(actual,p)]
for i in ans:
    print(i, end = " ")
