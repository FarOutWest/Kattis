#! usr/bin/env Python3
s = input()
zoom = len(s)
x, y = 0, 0
for i in range(zoom):
    let = int(s[zoom-i-1])
    if let == 0: pass
    elif let == 1: x += int((2**(i+1))/2)
    elif let == 2: y += int((2**(i+1))/2)
    elif let == 3:
        x += int((2**(i+1))/2)
        y += int((2**(i+1))/2)

print(zoom, x, y)
