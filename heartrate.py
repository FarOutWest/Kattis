for i in range(int(input())):
    bp = [float(a) for a in input().split()]
    print((60*bp[0])/bp[1] - 60/bp[1], 60/(bp[1]/bp[0]), (60*bp[0])/bp[1] + 60/bp[1])
