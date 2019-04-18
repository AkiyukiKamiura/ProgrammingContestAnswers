# coding: utf-8

N, M = list(map(int, input().split(' ')))
colors = []
for i in range(N):
    row = list(input())
    row_color = [0, 0, 0]
    for c in row:
        if c == 'W': row_color[0] += 1
        elif c == 'B': row_color[1] += 1
        elif c == 'R': row_color[2] += 1
    colors.append(row_color)

min_diff = float('inf')
for blue_top in range(1, N-1):
    for red_top in range(blue_top+1, N):
        diff = 0
        for i in range(N):
            if i < blue_top:
                diff += colors[i][1] + colors[i][2]
            elif i < red_top:
                diff += colors[i][0] + colors[i][2]
            else:
                diff += colors[i][0] + colors[i][1]
        if diff < min_diff:
            min_diff = diff

print(min_diff)
