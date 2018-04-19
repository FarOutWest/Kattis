for i in range(int(input())):
    str = input().split()
    if str[0] == 'Simon' and str[1] == 'says':
        print(' '.join(str[2::]))
