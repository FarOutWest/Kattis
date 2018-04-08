#! usr/bin/env Python3
import sys
N = int(sys.stdin.readline().strip())
vals = []
for i in range(N):
    vals.append(int(sys.stdin.readline().strip()))
exps = [i%10 for i in vals]
vals = [i//10 for i in vals]
ans = 0

for i in range(N):
    ans = ans + (vals[i]**exps[i])
print(ans)
