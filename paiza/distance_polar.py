#! python3
# coding: utf-8

import math

N = int(input())
n_1, d_1 = input().split(' ')
n_2, d_2 = input().split(' ')
n_1, n_2 = int(n_1), int(n_2)

min_dist = float('inf')
if d_1 == d_2:
    min_dist = abs(n_1 - n_2)*100
elif (d_1 in 'NS' and d_2 in 'NS') or (d_1 in 'WE' and d_2 in 'WE'):
    min_dist = (n_1 + n_2)*100
else:
    turn_on = list(range(max(n_1, n_2)+1))
    for isec in turn_on:
        dist = 100*(abs(n_1-isec) + abs(n_2-isec)) + 100*isec*math.pi/2
        if dist < min_dist: min_dist = dist

print(min_dist)
