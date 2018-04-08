#! usr/bin/env Python3
import sys
C = float(sys.stdin.readline().strip())
L = int(sys.stdin.readline().strip())
s = []
for i in range(L):
    s.append(sys.stdin.readline().split())
s = [float(i) for x in s for i in x]
first = []
second = []
for i in range(len(s)):
    if i % 2 == 0: first.append(s[i])
    else: second.append(s[i])
ans = [a*b*C for a,b in zip(first,second)]
print(sum(ans))
