#! /usr/bin/env python3
import sys

#read in X, Y, Z
inputs = sys.stdin.readline().strip().split()
x = int(inputs[0])
y = int(inputs[1])
z = int(inputs[2])
z += 1

#if i through Z is divisible by X print fizz, by Y buzz, or by both print fizzbuzz if not print i
for i in range(1, z):
    if i % x == 0 and i % y == 0:
        print('fizzbuzz')
        continue
    if i % x == 0:
        print('fizz')
    if i % y == 0:
        print('buzz')
    if i % x != 0 and i % y != 0:
        print(i)
