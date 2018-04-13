n = int(input())
s = [i for i in input()]
a = ['A','B','C']*n
b = ['B', 'A', 'B', 'C']*n
g = ['C', 'C', 'A', 'A', 'B', 'B']*n
ans, ansa, ansb, ansg = [], 0, 0, 0
for i in range(n):
    if s[i] == a[i]: ansa += 1
    if s[i] == b[i]: ansb += 1
    if s[i] == g[i]: ansg += 1
ans.append(ansa)
ans.append(ansb)
ans.append(ansg)
big = max(ans)
print(big)
if big == ansa: print('Adrian')
if big == ansb: print('Bruno')
if big == ansg: print('Goran')
