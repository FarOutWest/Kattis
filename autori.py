#! usr/bin/env Python3
import sys
a = sys.stdin.readline().strip()
print(''.join([c for c in a if c.isupper()]))
