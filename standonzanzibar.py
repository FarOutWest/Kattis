import sys
t = int(input())
ans = []
for i in range(t):
    imports = 0
    case = sys.stdin.readline().split()
    case = [int(a) for a in case if a != '0']
    for n in range(len(case) - 1):
        if case[n] <= (case[n+1]/2): imports += (case[n+1] - (2*case[n]))
    ans.append(imports)
for i in ans:
    print(i)
