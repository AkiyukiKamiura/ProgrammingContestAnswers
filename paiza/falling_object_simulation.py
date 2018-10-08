#! python3
# coding: utf-8

H, W, N = list(map(int, input().split(' ')))
field = [['.' for w in range(W)] for h in range(H)]

for n in range(N):
    h, w, x = list(map(int, input().split(' ')))
    check_columns = list(range(x, x+w))
    stacking_top = H
    for col in check_columns:
        for y in range(H):
            if field[y][col] == '#':
                if y < stacking_top: stacking_top = y
                break
    for i in range(stacking_top-h, stacking_top):
        for j in range(x, x+w):
            field[i][j] = '#'

for row in field:
    print(''.join(row))
