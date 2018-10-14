#! python3
# coding: utf-8

import numpy as np

H, W = list(map(int, input().split(' ')))
field = [list(input()) for i in range(H)]

def explosion(h, w, p):
    global field
    field[h][w] = 'b'
    pos = np.array([h, w])
    dirs = [np.array([1, 0]), np.array([-1, 0]), np.array([0, 1]), np.array([0, -1])]
    for dir in dirs:
        for i in range(1, p+1):
            new_pos = pos + dir*i
            if field[new_pos[0]][new_pos[1]] == '#': break
            elif field[new_pos[0]][new_pos[1]] == '.' or field[new_pos[0]][new_pos[1]] == 'X':
                field[new_pos[0]][new_pos[1]] = 'b'

enemies = []
for h in range(H):
    for w in range(W):
        if field[h][w] == 'X':
            enemies.append([h, w])
        elif field[h][w] != '#' and field[h][w] != 'b' and field[h][w] != '.':
            p = int(field[h][w])
            explosion(h, w, p)

ans = 'YES'
for enem in enemies:
    h, w = enem
    if field[h][w] == 'X':
        ans = 'NO'
        break

print(ans)
