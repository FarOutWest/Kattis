while True:
    case = input()
    if case == '0': break
    else:
        case = [float(i) for i in case.split()]
        x1, y1, x2, y2, p = case[0], case[1], case[2], case[3], case[4]
        ans = pow((pow(abs(x1-x2),p) + pow(abs(y1-y2),p)),1/p)
        print(ans)
