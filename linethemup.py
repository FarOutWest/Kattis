names, ans = [], ''
for i in range(int(input())): names.append(input())
for i in range(len(names)):
    if i != len(names)-1:
        if names[i] > names[i+1]:
            if ans == '' or ans == 'DECREASING': ans = 'DECREASING'
            else:
                ans = 'NEITHER'
                break
        else:
            if ans == '' or ans == 'INCREASING': ans = 'INCREASING'
            else:
                ans = 'NEITHER'
                break
print(ans)
