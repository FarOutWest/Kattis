#! usr/bin/env Python3
import sys
rev = []
nad = []
wad = []
n = int(sys.stdin.readline().strip())
for i in range(n):
    rev.append(sys.stdin.readline().split())
rev = [int(i) for a in rev for i in a]
nad = rev[0::3]
del rev[0::3]
wad = rev[0::2]
del rev[0::2]
wad = [b - a for a, b in zip(rev, wad)]
for i in range(n):
    if nad[i] > wad[i]: print('do not advertise')
    elif wad[i] > nad[i]: print('advertise')
    else: print('does not matter')
