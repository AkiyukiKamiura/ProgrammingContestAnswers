# coding: utf-8

H, W, N = list(map(int, input().split(' ')))
cards = [['.' for i in range(W+2)]]
for i in range(H):
    tmp = ['.']
    tmp.extend(input().split(' '))
    tmp.append('.')
    cards.append(tmp)
cards.append(['.' for i in range(W+2)])
pairs = [list(map(int, input().split(' '))) for i in range(N)]

for row in cards:
    print(' '.join(row))


def search_path(a, b, A, B):
    # 幅優先探索してみる
    
