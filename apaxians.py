name = input()
ans = ''
for i in range(len(name)):
    if i == 0: ans += name[i]
    else:
        if name[i] != name[i-1]: ans += name[i]
print(ans)
