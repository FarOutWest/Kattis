#! usr/bin/env Python3
import sys
N = int(sys.stdin.readline().strip())
N = bin(N)[2:]
N = N[::-1]
print(int(N,2))
