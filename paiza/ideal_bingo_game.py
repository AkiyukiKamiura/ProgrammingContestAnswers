#! python3
# coding: utf-8

N, M = list(map(int, input().split(' ')))
bingo_card = [list(map(int, input().split(' '))) for i in range(N)]
col_line_holes = [0 for i in range(N)]
row_line_holes = [0 for i in range(N)]
slanting_line_holes = [0, 0]

for i in range(M-1):
    num = int(input())
    for r in range(N):
        for c in range(N):
            if bingo_card[r][c] == num:
                bingo_card[r][c] = 0
                col_line_holes[c] += 1
                row_line_holes[r] += 1
                if r == c: slanting_line_holes[0] += 1
                if r + c == N-1: slanting_line_holes[1] += 1

bingos = 0
reachs = {}
for col, holes in enumerate(col_line_holes):
    if holes == N: bingos += 1
    elif holes == N-1:
        for r in range(N):
            if bingo_card[r][col] != 0:
                if (r, col) in reachs: reachs[(r, col)] += 1
                else: reachs[(r, col)] = 1
                break

for row, holes in enumerate(row_line_holes):
    if holes == N: bingos += 1
    elif holes == N-1:
        for c in range(N):
            if bingo_card[row][c] != 0:
                if (row, c) in reachs: reachs[(row, c)] += 1
                else: reachs[(row, c)] = 1
                break

for holes in slanting_line_holes:
    if holes == N: bingos += 1

if slanting_line_holes[0] == N-1:
    for i in range(N):
        if bingo_card[i][i] != 0:
            if (i, i) in reachs: reachs[(i, i)] += 1
            else: reachs[(i, i)] = 1
            break

if slanting_line_holes[1] == N-1:
    for i in range(N):
        if bingo_card[i][N-1-i] != 0:
            if (i, N-1-i) in reachs: reachs[(i, N-1-i)] += 1
            else: reachs[(i, N-1-i)] = 1
            break

max_bingos = 0
for key, val in reachs.items():
    if max_bingos < val: max_bingos = val
max_bingos += bingos

print(max_bingos)
