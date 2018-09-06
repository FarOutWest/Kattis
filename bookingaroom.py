r, n = input().split()
r, n, booked = int(r), int(n), []
for i in range(n): booked.append(int(input()))
if r == n: print('too late')
else:
    for i in range(1, r+1):
        if i not in booked:
            print(i)
            break
