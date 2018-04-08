#! usr/bin/env Python3
import sys
vals = []
speeds = []
times = []
ans = []
while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    else:
        for i in range(n):
            vals.append(sys.stdin.readline().split())
        vals = [int(i) for x in vals for i in x]
        for i in range(len(vals)):
            if i % 2 == 0: speeds.append(vals[i])
            else: times.append(vals[i])
        temp = [times[0]]
        times = [y - x for x, y in zip(times,times[1:])]
        times = temp + times
        distance = [a*b for a, b in zip(speeds,times)]
        ans.append(sum(distance))
        vals = []
        times = []
        speeds = []
        distance = 0
for a in ans:
    print(a, " miles")
