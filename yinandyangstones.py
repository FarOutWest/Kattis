stones = [a for a in input().strip()]
w, b = 0, 0
for a in stones:
    if a == 'W': w += 1
    else: b += 1
if w == b: print(1)
else: print(0)
