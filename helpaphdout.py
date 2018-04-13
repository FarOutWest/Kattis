n = int(input())
for i in range(n):
    nums = input().split('+')
    if nums[0] == 'P=NP': print('skipped')
    else: print(int(nums[0]) + int(nums[1]))
