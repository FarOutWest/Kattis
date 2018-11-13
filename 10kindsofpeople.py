def counter():
    i = 0
    while True:
        yield i
        i += 1

R, C = map(int, raw_input().split())
# uf = UnionFind()
type_grid = [[None]*C for _ in range(R)]
for r in range(R):
    l = raw_input()
    for c in range(C):
        type_grid[r][c] = l[c]

col_grid = [[None]*C for _ in range(R)]
count = counter()
for r in range(R):
    for c in range(C):
        if col_grid[r][c] is not None:
            continue

        fill = type_grid[r][c]
        color = next(count)
        q = [(r, c)]
        while q:
            r, c = q.pop()
            if col_grid[r][c] is not None:
                continue
            col_grid[r][c] = color

            if r + 1 < R and col_grid[r+1][c] is None and type_grid[r+1][c] == fill:
                q.append((r+1, c))
            if r - 1 >= 0 and col_grid[r-1][c] is None and type_grid[r-1][c] == fill:
                q.append((r-1, c))
            if c + 1 < C and col_grid[r][c+1] is None and type_grid[r][c+1] == fill:
                q.append((r, c+1))
            if c - 1 >= 0 and col_grid[r][c-1] is None and type_grid[r][c-1] == fill:
                q.append((r, c-1))

N = int(raw_input())
for _ in range(N):
    r1, c1, r2, c2 = map(lambda x: int(x) - 1, raw_input().split())
    if col_grid[r1][c1] != col_grid[r2][c2]:
        print('neither')
    else:
        print('decimal' if type_grid[r1][c1] == '1' else 'binary')
