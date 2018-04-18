a = [int(i) for i in input().split()]
parts = []
done = False
for i in range(a[1]):
    print('i = ', i)
    if input() not in parts:
        print('appended')
        parts.append(input())
    if len(parts) == a[0]:
        print(i+1)
        done = True
        break
if done == False: print('paradox avoided')
