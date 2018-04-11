import collections
nums = input().split()
nums = [int(i) for i in nums]
poss = []
sorted = []
most = []
ans = []
for i in range(nums[0]):
    for j in range(nums[1]): poss.append((i+1)+(j+1))
for i in range(max(poss)):
    for n in poss:
        if i == n: sorted.append(i)
for i in range(max(poss)): most.append(sorted.count(i+1))
ans = [i+1 for i, x in enumerate(most) if x == max(most)]
for i in ans: print(i)
