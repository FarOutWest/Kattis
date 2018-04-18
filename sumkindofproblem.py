p = int(input())
for i in range(p):
    kn = [int(a) for a in input().split()]
    print(kn[0], sum(range(0,kn[1]+1)), kn[1]**2, kn[1]*(kn[1]+1))
