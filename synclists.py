#! usr/bin/env Python3
def synchronize(l1, l2):
    mapping = dict(zip(sorted(l1), sorted(l2)))
    return [mapping[x] for x in l1]

while True:
    n = int(input())
    if n != 0:
        listOne, listTwo = [], []
        for i in range(n): listOne.append(int(input()))
        for i in range(n): listTwo.append(int(input()))
        ans = (synchronize(listOne, listTwo))
        for i in range(len(ans)):
            print(ans[i])
    else: break
