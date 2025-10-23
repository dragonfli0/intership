n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

row_max = []
for row in grid:
    plus = row.count('+')
    minus = row.count('-')
    quest = row.count('?')
    max_sum = plus - minus + quest
    row_max.append(max_sum)

col_min = []
for j in range(m):
    plus = 0
    minus = 0
    quest = 0
    for i in range(n):
        if grid[i][j] == '+':
            plus += 1
        elif grid[i][j] == '-':
            minus += 1
        else:
            quest += 1
    min_sum = plus - minus - quest
    col_min.append(min_sum)

max_r = max(row_max)
min_c = min(col_min)
print(max_r - min_c)
