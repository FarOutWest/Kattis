#! usr/bin/env Python3
import sys
vals = sys.stdin.readline().split()
vals = [i[::-1] for i in vals]
vals = [int(i) for i in vals]
if vals[0] > vals[1]: print(vals[0])
else: print(vals[1])
