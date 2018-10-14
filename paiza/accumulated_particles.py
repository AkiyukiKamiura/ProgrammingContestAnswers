#! python3
# coding: utf-8

H, W, N = list(map(int, input().split(' ')))
field = [[1001 if i == 0 or i == H+1 or j == 0 or j == W+1 else 0 for j in range(W+2)] for i in range(H+2)]

def fall(x, y):
    global field
    if field[y][x] == 0:
        field[y][x] += 1
    else:
        if field[y-1][x] < field[y][x]:
            fall(x, y-1)
        elif field[y][x+1] < field[y][x]:
            fall(x+1, y)
        elif field[y+1][x] < field[y][x]:
            fall(x, y+1)
        elif field[y][x-1] < field[y][x]:
            fall(x-1, y)
        else:
            field[y][x] += 1

for n in range(N):
    x, y = list(map(int, input().split(' ')))
    fall(x, y)

for i in range(1, H+1):
    print(' '.join(list(map(str, field[i][1:W+1]))))
