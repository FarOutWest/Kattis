import sys
p = sys.stdin.read().split('\n')
n, m, ans = 0, 0, []
for l in p:
    if len(l) > n: n = len(l)
for l in p: ans.append((n - len(l))**2)
ans = ans[:-2]
print(sum(ans))
