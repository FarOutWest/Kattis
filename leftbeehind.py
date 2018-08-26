while True:
    x, y = input().split()
    x, y = int(x), int(y)
    ans = ''
    if x == 0 and y == 0: break
    if x + y == 13: ans = 'Never speak again.'
    if ans != 'Never speak again.':
        if x > y: ans = 'To the convention.'
        if x < y: ans = 'Left beehind.'
        if x == y: ans = 'Undecided.'
    print(ans)
