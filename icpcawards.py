#! usr/bin/env Python3
won = set()
counter = 0
teams = []
for i in range(int(input())):
    s = input()
    if counter == 12:
        continue
    a, b = tuple(s.split())
    if a not in won:
        teams.append(s)
        won.add(a)
        counter += 1
print('\n'.join(teams))
