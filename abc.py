nums = sorted([int(i) for i in input().split()])
ans = []
order = input()
for ch in order:
    if ch == 'A': ans.append(str(nums[0]))
    elif ch == 'C': ans.append(str(nums[2]))
    elif ch == 'B': ans.append(str(nums[1]))
print(' '.join(ans))
