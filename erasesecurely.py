n = int(input())
before = input().strip()
after = int(input())
flipped = [i for i in before]

for i in range(n):
    for i in range(len(flipped)):
        if flipped[i] == '1': flipped[i] = '0'
        else: flipped[i] = '1'

if int(''.join(flipped)) == after: print('Deletion succeeded')
else: print('Deletion failed')
