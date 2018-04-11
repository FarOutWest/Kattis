word = input()
length = int(len(word)/3)
pers = ''
for i in range(length): pers = pers + 'PER'
ans = [i for a, b in zip(word, pers) if a != b]
print(len(ans))
