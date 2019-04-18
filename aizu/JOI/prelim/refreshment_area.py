# coding: utf-8

N, M, D = list(map(int, input().split(' ')))
field = [list(input()) for i in range(N)]

pattern_num = 0
cont = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == '.':
            cont += 1
            if cont >= D: pattern_num += 1
        else:
            cont = 0
    cont = 0

cont = 0
for j in range(M):
    for i in range(N):
        if field[i][j] == '.':
            cont += 1
            if cont >= D: pattern_num += 1
        else:
            cont = 0
    cont = 0

print(pattern_num)
