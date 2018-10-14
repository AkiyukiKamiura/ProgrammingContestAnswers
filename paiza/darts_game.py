#! python3
# coding: utf-8

import math

o_y, s, theta = list(map(int, input().split(' ')))
x, y, r = list(map(int, input().split(' ')))

y_hit = o_y + x*math.tan(math.radians(theta)) - (9.8*x*x)/(2*s*s*pow(math.cos(math.radians(theta)), 2))

if abs(y_hit - y) <= r/2:
    print('Hit %.1f'%abs(y_hit - y))
else:
    print('Miss')
