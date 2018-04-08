#! /usr/bin/env python3
import sys, math

#Read in N, the number of distances the bot can shoot, then the next N lines the actual distances
shotdistances = []
N = sys.stdin.readline().strip()

for i in range(0,int(N)):
    shotdistances.append(sys.stdin.readline().strip())

maxshotdistance = max(shotdistances)

#Read in M, the number of lenghts of holes, then the next M lines the actual distances of the holes
holedistances = []
M = sys.stdin.readline().strip()

for i in range(0,int(M)):
    holedistances.append(sys.stdin.readline().strip())

#given two shots check if you can reach the hole if so increment holes counter by one else increment the counter 0
holes = 0
index = 0

for i in holedistances:
    if int(maxshotdistance)*2 < int(i):
        holedistances.remove(i)
    if i in shotdistances:
        holedistances.remove(i)
        holes += 1

for s in range(0,len(shotdistances)):
    for a in range(0 + index,len(shotdistances)):
        sumofdist = int(shotdistances[s]) + int(shotdistances[a])
        if str(sumofdist) in holedistances:
            holedistances.remove(str(sumofdist))
            holes += 1
    index = index + 1

#print the holes counter on a single line
print(holes)
