#! usr/bin/env Python3
import sys
cards = sys.stdin.readline().strip()
tcount = 0
ccount = 0
gcount = 0
for i in cards:
    if i == 't' or i == 'T':
        tcount += 1
    elif i == 'c' or i == 'C':
        ccount += 1
    elif i == 'g' or i == 'G':
        gcount += 1
ans = 0
if tcount > 0 and ccount > 0 and gcount > 0:
    small = min(tcount,ccount,gcount)
    ans = 7 * small
ans = ans + (tcount**2) + (ccount**2) + (gcount**2)
print(ans)
