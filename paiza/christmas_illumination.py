#! python3
# coding: utf-8

import math

N = int(input())
trees = [list(map(int, input().split(' '))) for i in range(N)]

max_cls_num = 0

def get_range(x, y, r):
    a = math.sqrt(r**2 - y**2)
    return (x-a, x+a)

rans = {}
for tree in trees:
    tx, ty, tr = tree
    rl, ru = get_range(tx, ty, tr)

    for ran, count in rans:
        nl, nu = ran
        if
