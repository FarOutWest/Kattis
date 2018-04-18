a, b, c = [], [], []
while True:
    n = int(input())
    if n == 0: break
    else:
        for i in range(n*2):
            a.append(int(input()))
        for i in range([:1/2*len(a)]): b.append(a[i])
        for i in range([1/2*len(a):]): c.append(a[i])
