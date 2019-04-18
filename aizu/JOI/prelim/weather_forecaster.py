# coding: utf-8

H, W = list(map(int, input().split(' ')))
sections = [list(input()) for i in range(H)]

crowds = [[-1 for w in range(W)] for h in range(H)]

for h in range(H):
    c = -1
    for w in range(W):
        if c >= 0: c += 1
        if sections[h][w] == 'c': c = 0
        crowds[h][w] = c

for row in crowds:
    print(' '.join(list(map(str, row))))
