nums = []
ans = 0.0
for i in range(int(input())):
    nums = input().split()
    ans =  ans + (float(nums[0]) * float(nums[1]))
print("{:.3f}".format(ans))
