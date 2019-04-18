#! python3
# coding: utf-8

import math

W, H, M, N = list(map(int, input().split(' ')))
cams = [list(map(int, input().split(' '))) for i in range(M)]
items = [list(map(int, input().split(' '))) for i in range(N)]

def is_secure(a, b, x, y, t, d, r):
    dist = math.sqrt((x-a)**2 + (y-b)**2)
    if dist > r:
        return False #円の外にある
    theta = math.degrees(math.atan2(b-y, a-x))
    if theta < 0: theta += 360

    lower = t - d/2
    upper = t + d/2
    if lower < 0 and lower <= theta - 360: theta -= 360
    if upper >= 360 and upper >= theta + 360: theta += 360
    if lower <= theta and theta <= upper:
        return True
    else:
        return False

for item in items:
    flg = False
    for cam in cams:
        a, b = item
        x, y, t, d, r = cam
        if is_secure(a, b, x, y, t, d, r):
            flg = True
            break
    if flg:
        print('yes')
    else:
        print('no')
