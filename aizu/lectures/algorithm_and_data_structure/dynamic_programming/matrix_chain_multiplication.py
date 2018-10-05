#! python3
# matrix_chain_multiplication.py

INFTY = float('inf')

n = int(input())
M = [[0 for i in range(n)] for i in range(n)]
p = []

for i in range(n):
    r, c = list(map(int, input().split(' ')))
    if i == 0: p.append(r)
    p.append(c)

for i in range(n-1):
    M[i][i+1] = p[i]*p[i+1]*p[i+2]

for gap in range(2,n): # gap = 1,.., n-1
    for i in range(n-gap):
        j = i+gap
        M[i][j] = INFTY
        for k in range(i, j):
            M[i][j] = min([M[i][j], M[i][k] + M[k+1][j] + p[i]*p[k+1]*p[j+1]])

print(M[0][n-1])
