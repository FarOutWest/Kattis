#! usr/bin/env Python3
import sys
vals = sys.stdin.readline().split()
vals = [int(i) for i in vals]
print(vals[0] * (vals[1] - 1) + 1)
