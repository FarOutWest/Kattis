n = int(input())
b = []
ans = []
temp = ''
for i in range(n):
    b.append(input())
    b.append(input())
a = [i for i in b[0::2]]
del b[0::2]
for x, y in zip(a, b):
    for chx, chy in zip(x, y):
        if chx == chy: temp = temp + '.'
        else: temp = temp + '*'
    ans.append(temp)
    temp = ''
for i in range(n):
    print(a[i])
    print(b[i])
    print(ans[i], '\n')
