#! usr/bin/env Python3
import sys, math
vals = sys.stdin.readline().split()
vals = [int(i) for i in vals]
h = vals[0] / math.sin(math.radians(vals[1]))
print(math.ceil(h))
