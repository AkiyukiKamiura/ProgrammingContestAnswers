#! python3
# coding: utf-8

import copy

H, W, N = list(map(int, input().split(' ')))
fields = [['.' for w in range(W+2)] for h in range(H+2)]
remain_areas = H*W
for n in range(N):
    a, x, y = input().split(' ')
    fields[int(y)][int(x)] = a
    remain_areas -= 1

while remain_areas > 0:
    new_fields = copy.deepcopy(fields)
    for h in range(1, H+1):
        for w in range(1, W+1):
            if fields[h][w] ==  ".":
                around_areas = [fields[h-1][w], fields[h+1][w], fields[h][w-1], fields[h][w+1]]
                around_areas = list(set(around_areas))
                if '.' in around_areas: around_areas.remove('.')
                if len(around_areas) == 1:
                    new_fields[h][w] = around_areas[0]
                    remain_areas -= 1
                elif len(around_areas) >= 2:
                    new_fields[h][w] = '?'
                    remain_areas -= 1
    fields = new_fields

for row in fields[1:H+1]:
    print(''.join(row[1:W+1]))
