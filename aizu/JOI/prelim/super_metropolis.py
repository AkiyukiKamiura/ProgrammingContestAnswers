# coding: utf-8

INF = 10001
W, H, N = list(map(int, input().split(' ')))
cities = [list(map(int, input().split(' '))) for i in range(N)]

ways = 0
city = 1
while city < N:
    sx, sy = cities[city-1]
    gx, gy = cities[city]
    distx, disty = gx-sx, gy-sy
    if distx * disty > 0:
        tmp = min(abs(disty), abs(distx))
        ways += tmp
        distx -= tmp * int(distx/abs(distx))
        disty -= tmp * int(disty/abs(disty))
    ways += abs(distx) + abs(disty)
    city += 1
print(ways)
