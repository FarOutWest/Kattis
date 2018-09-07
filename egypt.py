while True:
    tri = sorted([int(a) for a in input().split()])
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0: break
    elif (tri[0]*tri[0]) + (tri[1]*tri[1]) == (tri[2]*tri[2]): print('right')
    else: print('wrong')
