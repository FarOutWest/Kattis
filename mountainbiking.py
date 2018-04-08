#! /usr/bin/env python3
import sys
import math

#read in the number of line segments N (1<=N<=4) and gravity (1<=g<=100) coefficient g in the same line
#split and convert each into int values
line = sys.stdin.readline().strip().split()
N = int(line[0])
G = int(line[1])

#read in N more lines containing D (1 <= D <= 10,000) the sloped distance in meters
#read in A (1 <= A <= 89) the absolute angle in degrees
#these segments are ordered from top to bottom
segments = []
distances = []
angles = []
for x in range(0,N):
    segments.append(sys.stdin.readline().strip().split())

for i in range(0,N):
    distances.append((segments[i][0]))
    angles.append((segments[i][1]))
    
print("distances: ", distances)
print("angles: ", angles)

for i in distances:
    if i.isdigit():
        i = int(i)
        if i < 1 or i > 10000:
            exit()
    else:
        exit()

for i in angles:
    if i.isdigit():
        i = int(i)
        if i < 1 or i > 89:
            exit()
    else:
        exit()

#the biker accelerates at a rate of g * cos(A) ms^-2
accel = []
vi = [0]
vf = []

for i in angles:
    if i.isdigit():
        i = int(i)
        accel.append(G * math.cos(i))
print("Accelerations: ", accel)

#Velocity is calculated by vf = sqrt(2 * accel * (absoluteval(posfinal - posinitial)) + vi)
for i in distances:
    index = 0
    vindex = 0
    if i.isdigit():
        i = int(i)
        if index == 0:
            y = 0
            index += 1
        else:
            y = distances[index]
            index += 1
        for x in range(0,len(distances)):
            initialvel = vi[vindex]
            print("vindex = ", vindex)
            print("initialvel = ", initialvel)
            print("Vi: ", vi)
            finalvel = 2 * accel[x] * ((abs(i - y)) + initialvel)
            if finalvel > 0:
                finalvel = math.sqrt(finalvel)
            else:
                finalvel = abs(finalvel)
                math.sqrt(finalvel)
            vf.append(finalvel)
            vindex += 1
            vi.append(vf)
    else:
        exit()

print("Vi: ", vi)
print("Vf: ", vf)

#Output N lines of data using real numbers that represent the velocity of the biker
# at the bottom of each line segment
print(vf)
