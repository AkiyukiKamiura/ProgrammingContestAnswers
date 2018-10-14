#! python3
# coding: utf-8

M, N = list(map(int, input().split(' ')))

m = 0
for i in range(100):
    flag = False
    for j in range(100-i):
        if M <= m:
            flag = True
            break
        print(i, '+', j, '=')
        m += 1
    if flag: break

n = 0
for i in range(99, -1, -1):
    flag = False
    for j in range(i+1):
        if N <= n:
            flag = True
            break
        print(i, '-', j, '=')
        n += 1
    if flag: break
