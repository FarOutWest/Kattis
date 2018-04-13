n = int(input())
ans = []
for i in range(n):
    nums = input().split()
    nums = [int(i) for i in nums]
    if (nums[0] + nums[1] == nums[2]) or (nums[0] - nums[1] == nums[2]) or (nums[0] * nums[1] == nums[2]) or (nums[0] / nums[1] == nums[2]) or (nums[1] - nums[0] == nums[2]) or (nums[1] / nums[0] == nums[2]): ans.append('Possible')
    else: ans.append('Impossible')
for i in ans:
    print(i)
