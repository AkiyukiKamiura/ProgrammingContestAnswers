# coding: utf-8

A, B, C, D, E = [int(input()) for i in range(5)]

time = 0
if A < 0: time += (min(B, 0) - A)*C
if A*B <= 0: time += D
if B > 0: time += (B - max(A, 0))*E
print(time)
