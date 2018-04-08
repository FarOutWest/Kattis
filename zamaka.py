#! usr/bin/env Python3
import sys
L = int(sys.stdin.readline().strip())
D = int(sys.stdin.readline().strip())
X = int(sys.stdin.readline().strip())

#find min
for i in range(L,D):
    i = str(i)
    i = [int(x) for x in i]
    if sum(i) == X:
        N = i
        N = [str(i) for i in N]
        print(''.join(N))
        break

#find max
for i in range(D,L,-1):
    i = str(i)
    i = [int(x) for x in i]
    if sum(i) == X:
        M = i
        M = [str(i) for i in M]
        print(''.join(M))
        break
