while True:
    a = [int(i) for i in input().split()]
    if a[0] == 0 and a[1] == 0: break
    else: print(int(a[0]/a[1]), a[0]%a[1], "/", a[1])
