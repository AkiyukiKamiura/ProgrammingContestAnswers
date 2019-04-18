# coding: utf-8

N = int(input())
mems = [list(map(int, input().split(' '))) for _ in range(N)]
points = [0 for _ in range(N)]

for i in range(3):
    turn = {}
    for j in range(N):
        if mems[j][i] not in turn: turn[mems[j][i]] = 0
        turn[mems[j][i]] += 1

    for j in range(N):
        if turn[mems[j][i]] == 1: points[j] += mems[j][i]

for point in points:
    print(point)
