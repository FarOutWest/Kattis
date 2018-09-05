import sys
for line in sys.stdin:
    line = line.lower()
    line = line.strip().split()
    ans = 'no'
    for word in line:
        if 'problem' in word:
            ans = 'yes'
            break
    print(ans)
