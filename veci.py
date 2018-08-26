num = input()
if ''.join(sorted(num, reverse=True)) == num:
    print (0)
else:
    for i in range(int(num)+1,999999):
        if sorted(num) == sorted(str(i)):
            print(i)
            break
