#! usr/bin/env Python3
import sys
n = sys.stdin.readline().split()
n = [int(i) for i in n]
if n[0] == 0 and n[1] == 0: print('Not a moose')
elif n[0] == n[1]: print('Even', 2 * max(n))
else: print('Odd', 2 * max(n))
