ans = 0
for i in range(int(input())):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a == b: ans += c
    
print(ans)
