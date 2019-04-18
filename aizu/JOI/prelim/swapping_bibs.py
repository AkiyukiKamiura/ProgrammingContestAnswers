# coding: utf-8

N, M = list(map(int, input().split(' ')))
A = [int(input()) for i in range(N)]

for k in range(1, M+1):
    i = 1
    while i != N:
        if A[i-1]%k > A[i]%k:
            A[i-1], A[i] = A[i], A[i-1]
        i += 1

for a in A: print(a)
