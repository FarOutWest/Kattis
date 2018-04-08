#! /usr/bin/env python3
import sys

#input the data each case as a line ended by the end of data
data = []
for index in range(0,10):
    data.append(sys.stdin.readline().split())
print(data)

#find the min, max, and range of each test case
maxes = []
mins = []
ranges = []

for a in data:
    maxes.append(max(a))
    mins.append(min(a))

for i in range(0,len(maxes)):
    ranges.append(maxes[i] - mins[i])

print("Maxes: ", maxes)
print("Mins: ", mins)
print("Ranges: ", ranges)

#print the data as 'Case X: # # #' where X is the case number and # are the min, max, and range
for i in len(maxes):
    print("Case", int(i), ":", int(mins[i]), int(maxes[i]), ranges[i])
