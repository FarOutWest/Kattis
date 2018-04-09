#! usr/bin/env Python3
import math
msg = input()
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
parta, partb = msg[:int(len(msg)/2)], msg[int(len(msg)/2):]
suma, sumb = 0, 0
for ch in parta: suma += alph.index(ch)
for ch in partb: sumb += alph.index(ch)
totshift = 0
newa = []
newb = []
ans = []
for ch in parta:
    totshift = suma + alph.index(ch)
    if totshift >= 26:
        subs = math.floor(totshift / 26)
        totshift -= (subs * 26)
        newa.append(alph[totshift])
for ch in partb:
    totshift = sumb + alph.index(ch)
    if totshift >= 26:
        subs = math.floor(totshift / 26)
        totshift -= (subs * 26)
        newb.append(alph[totshift])
newa = ''.join(newa)
newb = ''.join(newb)
for i in range(len(newa)):
    shift = alph.index(newb[i]) + alph.index(newa[i])
    if shift >= 26:
        subs = math.floor(shift / 26)
        shift -= (subs * 26)
        ans.append(alph[shift])
    else: ans.append(alph[shift])
print(''.join(ans))
