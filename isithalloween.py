date = input().split()
if date[0] == 'OCT':
    if date[1] == '31':
        print('yup')
    else:
        print('nope')
elif date[0] == 'DEC':
    if date[1] == '25':
        print('yup')
    else:
        print('nope')
else:
    print('nope')
