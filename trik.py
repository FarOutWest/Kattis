#! usr/bin/env Python3
import sys
moves = sys.stdin.readline().strip()
pos = 1
for i in moves:
    if pos == 1:
        if i == 'a' or i == 'A':
            pos = 2
        elif i == 'b' or i == 'B':
            pos = 1
        elif i == 'c' or i == 'C':
            pos = 3
    elif pos == 2:
        if i == 'a' or i == 'A':
            pos = 1
        elif i == 'b' or i == 'B':
            pos = 3
        elif i == 'c' or i == 'C':
            pos = 2
    elif pos == 3:
        if i == 'a' or i == 'A':
            pos = 3
        elif i == 'b' or i == 'B':
            pos = 2
        elif i == 'c' or i == 'C':
            pos = 1
print(pos)
