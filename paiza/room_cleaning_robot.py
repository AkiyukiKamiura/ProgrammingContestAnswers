#! python3
# coding: utf-8

seconds = int(input())
H, W = list(map(int, input().split(" ")))
spaces = [list(input()) for _ in range(H)]
cleaned_spaces = [[False for j in range(W)] for i in range(H)]

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
di = 0
x, y = 0, 0

cleaned = 0
for sec in range(seconds):
    if spaces[y][x] == '#': cleaned += 1
    cleaned_spaces[y][x] = True

    nx, ny = x, y
    while True:
        nx = x + dirs[di][1]
        ny = y + dirs[di][0]
        if nx >= W or ny >= H or cleaned_spaces[ny][nx]:
            di = di + 1 if di < 3 else 0
            next
        else:
            break

    x, y = nx, ny

print(cleaned)
