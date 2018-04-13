import sys, math
while True:
    a = [float(i) for i in sys.stdin.readline().split()]
    if a[0] == 0 and a[1] == 0: break
    else: print(round(pow((pow(a[0], 3) * math.pi / 6 - a[1]) / (math.pi / 6), 1.0/3), 9))
