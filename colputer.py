#! /usr/bin/env Python3
import sys
n = int(sys.stdin.readline().strip())
temps = sys.stdin.readline().split()
temps = [int(i) for i in temps]
tot = 0
for i in temps:
    if i < 0: tot += 1
print(tot)
