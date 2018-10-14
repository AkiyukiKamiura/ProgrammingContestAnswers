#! python3
# coding: utf-8

import numpy as np

H, W = list(map(int, input().split(' ')))
dungeon = [['w' for i in range(W+2)] for j in range(H+2)]
for h in range(H):
    row = input()
    for w in range(W):
        dungeon[h+1][w+1] = row[w]

pos = np.array(list(map(int, input().split(' '))))
N = int(input())
dirs = [input() for i in range(N)]
directions = {'U': np.array([0, -1]), 'R': np.array([1, 0]), 'D': np.array([0, 1]), 'L': np.array([-1, 0])}

for d in dirs:
    while True:
        next_pos = pos + directions[d]
        if dungeon[next_pos[1]][next_pos[0]] == "w": break
        if dungeon[next_pos[1]][next_pos[0]] == ".":
            pos = next_pos
            break
        pos = next_pos

print(pos[0], pos[1])
