ans = []
for i in range(10):
    n = int(input())
    ans.append(n%42)
print(len(set(ans)))
