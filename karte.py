P, K, H, T = 13, 13, 13, 13
s = input()
s = [s[i:i+3] for i in range(0, len(s), 3)]
for i in s:
    if len(s) != len(set(s)): do = False
    else:
        do = True
        if i.startswith("P"): P -= 1
        elif i.startswith("K"): K -= 1
        elif i.startswith("H"): H -= 1
        else: T -= 1
if do:
    print(P,K,H,T)
else: print('GRESKA')
