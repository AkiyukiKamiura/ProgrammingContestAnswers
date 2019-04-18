# coding: utf-8

N = int(input())
M = int(input())
A = list(map(int, input().split(' '))) # M個
B = [list(map(int, input().split(' '))) for i in range(M)]

scores = [0 for i in range(N)]
for i in range(M):
    target = A[i]
    for j in range(N):
        if B[i][j] == target:
            scores[j] += 1
        else:
            scores[target-1] += 1

for score in scores:
    print(score)
