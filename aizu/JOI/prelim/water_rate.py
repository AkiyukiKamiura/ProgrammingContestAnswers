# coding: utf-8

A, B, C, D, P = [int(input()) for i in range(5)]
cost = B + max(0, P - C)*D
cost = A*P if A*P < cost else cost
print(cost)
