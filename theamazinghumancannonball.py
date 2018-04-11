import math
n = int(input())
cases = []
ans = []
for i in range(n):
    cases.append(input().split())
for case in cases:
    v = float(case[0])
    cosa = math.cos(math.radians(float(case[1])))
    sina = math.sin(math.radians(float(case[1])))
    x = float(case[2])
    h1 = float(case[3]) + 1
    h2 = float(case[4]) - 1
    g = (9.81/2)
    t = (x / cosa) / v
    y = v * t * sina - (g * (t**2))
    if y >= h1 and y <= h2: ans.append('Safe')
    else: ans.append('Not Safe')
for i in ans:
    print(i)
