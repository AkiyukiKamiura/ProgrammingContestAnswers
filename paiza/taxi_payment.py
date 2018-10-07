#! python3

import math

N, X = list(map(int, input().split(' ')))
max_payment, min_payment = 0, float('inf')
for n in range(N):
    a, b, c, d = list(map(int, input().split(' ')))
    payment = 0
    if X < a:
        payment = b
    else:
        payment = b + math.ceil((X-a+1)/c)*d
    if max_payment < payment:
        max_payment = payment
    if payment < min_payment:
        min_payment = payment

print(min_payment, max_payment)
