#! python3
# coding: utf-8

import numpy as np

N, K = list(map(int, input().split(' ')))
original_image = np.array([list(map(int, input().split(' '))) for i in range(N)])
new_size = int(N/K)
new_image = [[0 for c in range(new_size)] for r in range(new_size)]

for r in range(new_size):
    for c in range(new_size):
        base_r, base_c = r*K, c*K
        new_image[r][c] = int(np.floor(np.mean(original_image[base_r:base_r+K, base_c:base_c+K])))

for row in new_image:
    print(' '.join(list(map(str, row))))
