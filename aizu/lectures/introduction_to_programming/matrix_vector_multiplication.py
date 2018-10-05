#! python3
# matrix_vector_multiplication.py

n, m = list(map(int, input().split(' ')))
a = [list(map(int, input().split(' '))) for i in range(n)]
b = [int(input()) for i in range(m)]

for i in range(n):
    rst = 0
    for j in range(m):
        rst += a[i][j] * b[j]
    print(str(rst))
