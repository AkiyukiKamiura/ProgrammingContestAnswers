#! python3
# coding: utf-8

import copy

L, n, m = list(map(int, input().split(' ')))
bridges = [[] for i in range(n-1)]
for i in range(m):
    a, b, c = list(map(int, input().split(' ')))
    bridges[a-1].append([b, c])

now_length = L
now_line = 0

while True:
    nearest_br_right = []
    nearest_br_left = []
    tmp = 0
    if now_line != n-1:
        brs = bridges[now_line]
        nearest_br_right = []
        for br in brs:
            if br[0] >= now_length: continue
            if br[0] > tmp:
                tmp = br[0]
                nearest_br_right = copy.copy(br)
    if now_line != 0:
        brs = bridges[now_line-1]
        nearest_br_left = []
        for br in brs:
            if br[1] >= now_length: continue
            if br[1] > tmp:
                tmp = br[1]
                nearest_br_left = copy.copy(br)

    if tmp == 0:
        break
    elif len(nearest_br_left) == 0:
        now_length = nearest_br_right[1]
        now_line += 1
    else:
        now_length = nearest_br_left[0]
        now_line -= 1

print(now_line+1)
