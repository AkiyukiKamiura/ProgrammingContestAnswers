# coding: utf-8

import math

L, A, B, C, D = [int(input()) for i in range(5)]
print(L - max(math.ceil(A/C), math.ceil(B/D)))
