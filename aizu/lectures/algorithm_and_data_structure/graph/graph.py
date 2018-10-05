#! python
# graph

n = int(input())
A = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    arr = list(map(int, input().split(' ')))
    u, k, v = arr[0], arr[1], arr[2:]
    for j in range(k):
        A[u-1][v[j]-1] = 1

for li in A:
    print(' '.join(list(map(str, li))))
