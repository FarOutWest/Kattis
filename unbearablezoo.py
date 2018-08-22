import collections
list = 1
while True:
    num = int(input())
    animals = []
    ans = []
    occur = 0
    if num == 0: break
    for i in range(num): animals.append(input().strip())
    for animal in animals:
        animal = animal.split()
        ans.append(animal[len(animal)-1])
    ans = sorted([a.lower() for a in ans])
    c = collections.Counter(ans)
    print("List ", list, ":", sep = "")
    for i in c:
        print(i, "|", c[i])
    list += 1
