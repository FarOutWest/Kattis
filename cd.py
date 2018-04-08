#! /usr/bin/env python3
import sys

#read in N then M the number of cd's owned by Jack then Jill
cdtot = sys.stdin.readline().strip().split()
N = cdtot[0]
M = cdtot[1]

#read in the cd's for Jack(N) then Jill(M) and index them
jacks = []
jills = []
for i in range(0,int(N)):
    jacks.append(sys.stdin.readline().strip())

for i in range(0,int(M)):
    jills.append(sys.stdin.readline().strip())

#print("Jacks: ", jacks)
#print("Jills: ", jills)

#compare the lists count the total number of differences
same = [item for item in jacks if item in jills]
#print("SAME: ", same)
#print("SAMELEN: ", len(same))

#print the total number of differences between N and M
if len(same)%2 != 0:
    samelen = len(same) - 1
    total = int(N) - (samelen/2)
else:
    total = int(N) - (len(same)/2)

print(int(total))
