import sys
ans = []
while True:
    n = sys.stdin.readline().strip()
    n1 = int(n)
    if n == '0':
        break
    else:
        n = [int(i) for i in n]
        sumn = sum(n)
        for i in range(11,100001):
            temp = i * n1
            temp = [int(t) for t in str(temp)]
            if sum(temp) == sumn:
                ans.append(i)
                break
for i in ans:
    print(i)
