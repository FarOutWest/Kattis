a = [int(i) for i in input().split()]
n, p, q = a[0], a[1], a[2]
if ((p+q)/n)%2 == 0: print('paul')
else: print('opponent')
