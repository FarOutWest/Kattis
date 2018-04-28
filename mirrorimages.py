for i in range(int(input())):
    line = []
    t = [int(a) for a in input().split()]
    for j in range(t[0]):
        line.append(input()[::-1])
    print('Test',i+1)
    for k in reversed(line):
        print(k)
