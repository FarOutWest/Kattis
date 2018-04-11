val = input().split()
n = int(val[0])
b = val[1]
hands = []
score = 0
dom = {'A': 11, 'K': 4, 'Q': 3, 'J': 20, 'T': 10, '9': 14, '8': 0, '7': 0}
nondom = {'A': 11, 'K': 4, 'Q': 3, 'J': 2, 'T': 10, '9': 0, '8': 0, '7': 0}
for i in range(4*n):
    hands.append(input())
hands = [hands[x:x+4] for x in range(0, len(hands),4)]
for i in hands:
    for a in i:
        firstpart, secondpart = a[:1], a[1:]
        if secondpart == b: score += dom[firstpart]
        else: score += nondom[firstpart]
print(score)
