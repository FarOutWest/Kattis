#! usr/bin/env Python3
import sys
stones = int(sys.stdin.readline().strip())
if stones % 2 == 0: print('Bob')
else: print('Alice')
