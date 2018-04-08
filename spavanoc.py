#! usr/bin/env Python3
import sys
sub = 45
time = sys.stdin.readline().split()
time = [int(i) for i in time]
if time[1] < sub:
    sub -= time[1]
    time[1] = 60 - sub
    if time[0] != 0:
        time[0] -= 1
    else: time[0] = 23
elif time[1] == sub:
    time[1] = 0
elif time[1] > sub:
    time[1] -= sub

time = [str(i) for i in time]
print(' '.join(time))
