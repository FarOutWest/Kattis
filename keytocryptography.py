cypher = [ch for ch in input().strip()]
secret = [ch for ch in input().strip()]
og_secret = secret
if len(secret) > len(cypher):
    for i in range(len(secret) - len(cypher)): secret.pop()
    og_secret = secret
shifts = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6,
          'H':7, 'I':8, 'J':9, 'K':10, 'L':11, 'M':12, 'N':13,
          'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 'T':19,'U':20,
          'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}
shiftnums, cyphernums, ans = [], [], []
cyphernums = [shifts.get(ch) for ch in cypher]
while len(ans) < len(cypher):
    secret = og_secret + ans
    shiftnums, ans = [], []
    shiftnums = [shifts.get(ch) for ch in secret]
    loop_to = len(secret)
    if len(cypher) < loop_to: loop_to = len(cypher)
    for i in range(loop_to):
        shift = cyphernums[i] - shiftnums[i]
        if shift < 0: shift = 26 + shift
        ans.append(list(shifts.keys())[list(shifts.values()).index(shift)])
print (''.join(ans))
