case = [int(i) for i in input().split()]
while case != sorted(case):
    for i in range(len(case)-1):
        if case[i] > case[i+1]:
            case[i], case[i+1] = case[i+1], case[i]
            print(*case)
