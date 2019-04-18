#! python3
# coding: utf-8

import numpy as np

board = [['x' if (i == 0 or i == 9 or j == 0 or j == 9) else '.' for i in range(10)] for j in range(10)]
board[5][4] = 'B'
board[4][5] = 'B'
board[4][4] = 'W'
board[5][5] = 'W'

def check_changing_index(x, y, c):
    directions = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1]),
                  np.array([1, 1]), np.array([-1, -1]), np.array([1, -1]), np.array([-1, 1])]
    pos = np.array([x, y])
    rst_index = []

    for di in directions:
        cur_pos = np.array([x, y]) + di
        flg = False
        while (board[cur_pos[1]][cur_pos[0]] != 'x' and board[cur_pos[1]][cur_pos[0]] != '.'):
            if (board[cur_pos[1]][cur_pos[0]] == c):
                flg = True
                break
            cur_pos += di
        if flg:
            cur_pos -= di
            while (board[cur_pos[1]][cur_pos[0]] != 'x' and board[cur_pos[1]][cur_pos[0]] != '.'):
                if (cur_pos == pos).all(): break
                rst_index.append((cur_pos[0], cur_pos[1]))
                cur_pos -= di
    return rst_index

N = int(input())
logs = [input() for i in range(N)]
stones = {'black': 2, 'white': 2}

for log in logs:
    c, x, y = log.split()
    x, y = int(x), int(y)
    board[y][x] = c
    change_indexes = check_changing_index(x, y, c)
    if len(change_indexes) == 0: continue
    for ci in change_indexes:
        board[ci[1]][ci[0]] = c
    if c == 'B':
        stones['black'] += len(change_indexes) + 1
        stones['white'] -= len(change_indexes)
    else:
        stones['white'] += len(change_indexes)+1
        stones['black'] -= len(change_indexes)

judged = 'Draw!'
if stones['black'] > stones['white']: judged = 'The black won!'
else: judged = 'The white won!'
print('%02d-%02d %s'%(stones['black'], stones['white'], judged))
