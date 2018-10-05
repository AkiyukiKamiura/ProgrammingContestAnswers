#! python3
# coin_changing_problem.py

n, m = list(map(int, input().split(' ')))
c = list(map(int, input().split(' ')))

table = [[0 for j in range(n+1)] for i in range(m+1)]
table[0][1:] = [float('inf') for j in range(1, n+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        if j - c[i-1] < 0:
            table[i][j] = table[i-1][j]
        else:
            table[i][j] = min(table[i-1][j], table[i][j-c[i-1]]+1)

print(table[-1][-1])
