game_time = 210
player = int(input())
for i in range(int(input())):
    #rint('player = ', player)
    q = input().split()
    t = int(q[0])
    game_time -= t
    if game_time <= 0: break
    if q[1] == 'T':
        if player != 8: player += 1
        else: player = 1
        #print('player += ', player)
print(player)
