#! /usr/bin/env python3
import sys

integers = []
tests = []
ans = []
yearlen = 1000000007

integers = sys.stdin.read().strip().split()
for x in integers:
    if x.isdigit():
        x = int(x)
        if x > 10000000:
            exit()
        if x != 0:
            tests.append(x)
        else:
            break
    else:
        exit()

if len(tests) > 25:
    exit()

print("INTEGERS: ", integers)
print("TESTS: ", tests)

for n in tests:
    n = int(n)
    ans.append(yearlen - n)

print("ANS: ", ans)
