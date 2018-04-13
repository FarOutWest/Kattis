line = input()
ws = 0
lower = 0
upper = 0
symbols = 0
length = len(line)
for ch in line:
    if ch == "_": ws += 1
    elif ch.islower(): lower += 1
    elif ch.isupper(): upper += 1
    else: symbols += 1
print(ws/length)
print(lower/length)
print(upper/length)
print(symbols/length)
