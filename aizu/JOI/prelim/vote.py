# coding: utf-8

N, M = list(map(int, input().split(' ')))
A = [int(input()) for _ in range(N)]
B = [int(input()) for _ in range(M)]
scores = [0 for _ in range(N)]

for j in range(M):
    for i in range(N):
        if A[i] <= B[j]:
            scores[i] += 1
            break

max_i, max_val = 0, 0
for i in range(N):
    if scores[i] > max_val:
        max_val = scores[i]
        max_i = i
print(max_i + 1)
