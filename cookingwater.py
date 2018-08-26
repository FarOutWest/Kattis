a, b = [], []
for i in range(int(input())):
    temp = []
    aa, bb = input().split()
    a.append(int(aa))
    b.append(int(bb))
if max(a) > min(b): print('edward is right')
else: print('gunilla has a point')
