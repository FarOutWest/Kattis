for i in range(int(input())):
    case = [int(i) for i in input().split()]
    del case[0]
    for a in range(len(case)):
        if (case[a]+1) != case[a+1]:
            print(a+2)
            break
