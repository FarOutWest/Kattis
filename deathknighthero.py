#! usr/bin/env Python3
ans = 0
n = int(input())
for i in range(n):
    a = input().strip()
    if "CD" not in a: ans += 1
print(ans)
