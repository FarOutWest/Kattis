#! usr/bin/env Python3
import sys, math
inputs = sys.stdin.readline().split()
N = int(inputs[0])
W = int(inputs[1])
H = int(inputs[2])
hyp = math.sqrt((W**2) + (H**2))
ans = []

for i in range(N):
    val = int(sys.stdin.readline().strip())
    if val <= hyp: ans.append('DA')
    else: ans.append('NE')
for i in ans:
    print(i)
