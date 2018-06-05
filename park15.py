abc = [int(i) for i in input().split()]
a, b, c, i = abc[0], abc[1], abc[2], 0
start, stop = [], []
for i in range(3):
    times = [int(j) for j in input().split()]
    start.append(times[0])
    stop.append(times[1])
cost = 0
for i in range(max(stop) + 1):
    parked = 0
    if (start[0] <= i and i < stop[0]):
        parked += 1
    if (start[1] <= i and i < stop[1]):
        parked += 1
    if (start[2] <= i and i < stop[2]):
        parked += 1
    if parked == 1: cost += a
    if parked == 2: cost += 2 * b
    if parked == 3: cost += 3 * c
print(cost)

#5+6+3+3+3+6+5+5
