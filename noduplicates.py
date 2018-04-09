#! usr/bin/env Python3
import sys
text = sys.stdin.readline().split()
if set([x for x in text if text.count(x) > 1]): print('no')
else: print('yes')
