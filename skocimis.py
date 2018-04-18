#! usr/bin/env Python3
abc = [int(i) for i in input().split()]
a, b, c = abc[0], abc[1], abc[2]
print(max(b - a, c - b) - 1)
