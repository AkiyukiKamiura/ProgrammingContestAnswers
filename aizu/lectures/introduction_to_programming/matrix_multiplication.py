#! python3
# matrix_multiplication.py

n, m, l = [int(x) for x in input().split(' ')]

mat1 = [[int(x) for x in input().split(' ')] for i in range(n)]
mat2 = [[int(x) for x in input().split(' ')] for j in range(m)]

rst_mat = [[0 for k in range(l)] for i in range(n)]

for i in range(n):
    for k in range(l):
        for j in range(m):
            rst_mat[i][k] += mat1[i][j] * mat2[j][k]

for i in range(n):
    print(' '.join([str(x) for x in rst_mat[i]]))
