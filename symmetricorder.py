import sys
ans = []
run = 0
while True:
    n = int(sys.stdin.readline().strip())
    if n == 0:
        break
    else:
        case = []
        front = []
        back = []
        run += 1
        for i in range(n):
            if i % 2 == 0: front.append(sys.stdin.readline().strip())
            else: back.insert(0, sys.stdin.readline().strip())
        ans = front + back
        print('SET ', run)
        for n in ans:
            print(n)
