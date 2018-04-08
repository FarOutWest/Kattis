#! usr/bin/env Python3
import sys
x = int(sys.stdin.readline().strip())
y = int(sys.stdin.readline().strip())

if x > 0 and y > 0: print(1)
if x < 0 and y > 0: print(2)
if x < 0 and y < 0: print(3)
if x > 0 and y < 0: print(4)
