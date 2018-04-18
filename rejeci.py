a, b = 1, 0
for i in range(int(input())):
    temp = a + b
    a = b
    b = temp
print(a,b)
