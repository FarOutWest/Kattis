#! usr/bin/env Python3
import sys
a = int(sys.stdin.readline().strip())
hits = sys.stdin.readline().split()
hits = [int(i) for i in hits]
for i in range(len(hits)):
    if hits[i] == -1:
        hits[i] = 0
        a -= 1
print(sum(hits)/a)
