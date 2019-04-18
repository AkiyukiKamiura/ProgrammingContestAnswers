#! python3
# coding: utf-8

H, W = list(map(int, input().split(' ')))
weather_map = [list(input()) for i in range(H)]
checked = [[False for j in range(W)] for i in range(H)]
dirs = {"R": (0, 1),
        "L": (0, -1),
        "U": (-1, 0),
        "D": (1, 0)}

loop = 0
for y in range(H):
    for x in range(W):
        if checked[y][x]: continue
        cx, cy = x, y
        dir = dirs[weather_map[cy][cx]]
        route = []

        while True:
            dir = dirs[weather_map[cy][cx]]
            nx, ny = cx + dir[1], cy + dir[0]
            if nx < 0 or nx >= W or ny < 0 or ny >= H: break
            if (nx, ny) in route:
                loop += 1
                break
            if checked[ny][nx]: break
            checked[ny][nx] = True
            route.append((cx, cy))

            cx, cy = nx, ny

print(loop)
