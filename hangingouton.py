a = input().split()
na = 0
on = 0
l, x = int(a[0]), int(a[1])
for i in range(x):
    dif = input().split()
    if dif[0] == 'enter':
        temp = on + int(dif[1])
        if temp <= l: on += int(dif[1])
        else: na += 1
    elif dif[0] == 'leave': on -= int(dif[1])
print(na)
