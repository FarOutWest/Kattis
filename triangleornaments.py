import math
ans = 0
for i in range(int(input())):
    a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    if a == b: ans += c
    C = math.acos((a*a + b*b - c*c) / (2 * a * b))
    B = math.acos((a*a + c*c - b*b) / (2 * a * c))
    bx = a * math.cos(B) + 100
    by = a * math.sin(B)
    cx = (0 + bx + c + 200) / 3
    cy = (0 + by + 0) / 3
    newAngle = math.pi / 2 - b
    degChange = newAngle - math.atan(abs(cx - bx) / abs(cy - by))
    v = abs(a * math.sin(degChange))
    ans += (v * 2)
print(ans)
