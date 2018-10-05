#! python 3
# distance_ii.py

import math

def minkovski(a, b, p):
    if p == 'inf':
        tmp_arr = [abs(x-y) for x, y in zip(a, b)]
        max_val = tmp_arr[0]
        for i in range(1, len(a)):
            if max_val < tmp_arr[i]:
                max_val = tmp_arr[i]
        return max_val
    else:
        dst = 0
        for x, y in zip(a, b):
            dst += pow(abs(x-y), p)
        dst = pow(dst, 1/p)
        return dst

n = int(input())
a = [int(x) for x in input().split(' ')]
b = [int(x) for x in input().split(' ')]

for p in [1, 2, 3, 'inf']:
    print('%.6f'%minkovski(a, b, p))
