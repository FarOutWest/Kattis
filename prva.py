r, c = input().split()
r, c = int(r), int(c)
raw_rows, rows, columns, word = [], [], [], ''
for i in range(r): raw_rows.append(input().strip())
for row in raw_rows:
    for ch in row.split('#'): rows.append(ch)
for i in range(c):
    for j in range(r):
        if raw_rows[j][i] != '#':
            word += raw_rows[j][i]
        else:
            if word != '':
                columns.append(word)
                word = ''
        if j == r-1:
            if word != '':
                columns.append(word)
                word = ''
columns = [a for a in columns if len(a) > 1]
ans = sorted([w for w in rows+columns if len(w) > 1])
print(ans[0])
