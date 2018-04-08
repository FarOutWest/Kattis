#! /usr/bin/env python3
import sys

L = int(sys.stdin.readline())
if L < 0:
    exit()

length = len(str(L))
n = L/length

print(int(n))
