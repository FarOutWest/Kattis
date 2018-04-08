#! /usr/bin/env python3
import sys

#get T the number of test cases
T = sys.stdin.readline()

#read in the test cases first line is the sounds
    #second line through last - 1 line is <animal> says <sound> GET SOUDS HERE
    #last line of input cases is 'what does the fox say?'
recordings = []
for index in range(0,int(T)):
    sounds = sys.stdin.readline().strip().split()
    print(sounds)

    while True:                                 ### <--- THIS DOES NOT WORK FIX HERE MATE
        line = sys.stdin.readline()
        if line == 'what does the fox say?':
            break
        else:
            recordings.append(line)

print(recordings)

#remove the sounds in sounds from recordings print those V
for i in range(0,int(T)):
    if recordings[i] in sounds[i]:
        sounds[i].remove()

#output the sounds that were not made by other animals in the test cases one per line
for i in range(0,int(T)):
    print(sounds[i])
