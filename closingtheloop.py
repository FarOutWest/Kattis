for i in range(int(input())):
    s = int(input())
    ropes = input().split()
    blue, red, numseg, ans = [], [], 0, 0
    for rope in ropes:
        if 'B' in rope: blue.append(int(rope[:-1]))
        else: red.append(int(rope[:-1]))
    blue, red = sorted(blue, reverse = True), sorted(red, reverse = True)
    numseg = min(len(blue), len(red))
    for j in range(numseg):
        ans += blue[j]
        ans += red[j]
    print('Case #', i+1, ': ', ans-(numseg*2), sep='')
