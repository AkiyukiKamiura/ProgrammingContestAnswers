#! python3
# coding: utf-8

import numpy as np

w, h, n = list(map(int, input().split(' ')))
x, y = list(map(int, input().split(' ')))
logs = [input().split(' ') for _ in range(n)]

dirs = {'D': np.array([0, -1]),
        'R': np.array([1, 0]),
        'U': np.array([0, 1]),
        'L': np.array([-1, 0])}
pos = np.array([x, y])

for log in logs:
    dir, amo = log[0], int(log[1])
    pos += amo * dirs[dir]
    pos[0] %= w
    pos[1] %= h

print(pos[0], pos[1])
