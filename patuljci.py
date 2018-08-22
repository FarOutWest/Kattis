import itertools
og, d, result = [], [], []
for i in range(9): og.append(int(input()))
d = sorted(og)
sum = sum(d)
diff = sum - 100
for i in range(len(d)):
    for j in range(i+1, len(d)):
        if d[i] + d[j] == diff: result = (d[i], d[j])
for r in result: og.remove(r)
for r in og: print(r)
