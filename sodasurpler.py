a = [int(i) for i in input().split()]
e, f, c = a[0], a[1], a[2]
e += f
drank = 0
while e >= c:
    new_sodas, remaining_empty = int(e/c), int(e%c)
    drank += new_sodas
    e = new_sodas + remaining_empty
print(int(drank))
