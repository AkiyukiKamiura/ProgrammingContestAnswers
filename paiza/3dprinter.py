#! python3
# coding: utf-8

X, Y, Z = list(map(int, input().split(' ')))
x_view = [['.' for y in range(Y)] for z in range(Z)]

for z in range(Z):
    for x in range(X):
        inp = input()
        for y in range(Y):
            if inp[y] == '#':
                x_view[z][y] = '#'
    input()

for z in x_view[::-1]:
    print(''.join(list(map(str, z))))
