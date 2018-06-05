import sys
words = sys.stdin.read().split()
ans = []
for i in range(len(words)):
    if i == len(words)-1: break
    if words[i] + words[i+1] not in ans: ans.append(words[i] + words[i+1])
for a in ans:
    print(a)
