#! python3
# coding: utf-8

import math

r = float(input())
scanning_grid = math.ceil(r)

half_quarter = 0
for x in range(scanning_grid):
    for y in range(x):
        if math.sqrt(x*x + y*y) < r:
            half_quarter += 1

quarter = half_quarter * 2
for x in range(scanning_grid):
    if math.sqrt(2*x*x) < r:
        quarter += 1

print(quarter * 4)
