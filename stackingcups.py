import collections
n = int(input())
d = {}
for i in range(n):
    temp = input().split()
    if temp[0].isdigit(): d[int(temp[0])/2] = temp[1]
    else: d[int(temp[1])] = temp[0]
d = collections.OrderedDict(sorted(d.items()))
for i, j in d.items(): print(j)
