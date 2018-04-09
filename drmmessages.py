#! usr/bin/env Python3
msg = input()
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
parta, partb = msg[:int(len(msg)/2)], msg[int(len(msg)/2):]
suma, sumb = 0, 0
for ch in parta:
    suma += alph.index(ch)
for ch in partb:
    sumb += alph.index(ch)
#shift function to shift each letter based on the sumvals
