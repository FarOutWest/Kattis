while True:
    N, M = input().split()
    N, M, jacks, jills = int(N), int(M), [], []
    if N == 0 and M == 0: break
    for i in range(N): jacks.append(input().strip())
    for i in range(M): jills.append(input().strip())
    sell, ni, mi = 0, 0, 0
    while (ni < N and mi < M):
        if jacks[ni] > jills[mi]: mi += 1
        elif jacks[ni] < jills[mi]: ni += 1
        else:
            sell, mi, ni = sell + 1, mi + 1, ni + 1
    print(sell)
