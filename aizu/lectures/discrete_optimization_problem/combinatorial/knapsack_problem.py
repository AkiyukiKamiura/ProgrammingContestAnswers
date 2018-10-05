#! python3

n, w = list(map(int, input().split(' ')))
items = [list(map(int, input().split(' '))) for i in range(n)]

table = [[0 for j in range(n+1)] for i in range(w+1)]

for i in range(1, w+1):
    for j in range(1, n+1):
        v, w = items[j-1]
        if i - w < 0:
            table[i][j] = table[i][j-1]
        else:
            new_val = table[i-w][j] + v
            table[i][j] = new_val if new_val > table[i][j-1] else table[i][j-1]

print(table[-1][-1])
