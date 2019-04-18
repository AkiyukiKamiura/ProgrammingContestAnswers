# coding: utf-8

import math

N, A, B, C, D = list(map(int, input().split(' ')))
price_X = B * math.ceil(N/A)
price_Y = D * math.ceil(N/C)
print(min(price_X, price_Y))
