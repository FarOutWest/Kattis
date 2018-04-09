#! usr/bin/env Python3
import sys
first = sys.stdin.readline().split()
first = [int(i) for i in first]
first = sum(first)
second = sys.stdin.readline().split()
second = [int(i) for i in second]
second = sum(second)
third = sys.stdin.readline().split()
third = [int(i) for i in third]
third = sum(third)
fourth = sys.stdin.readline().split()
fourth = [int(i) for i in fourth]
fourth = sum(fourth)
fifth = sys.stdin.readline().split()
fifth = [int(i) for i in fifth]
fifth = sum(fifth)

ans = max(first,second,third,fourth,fifth)
d = {'1': first, '2': second, '3': third, '4': fourth, '5': fifth}
d = max(d, key = d.get)
print(d, ans)
