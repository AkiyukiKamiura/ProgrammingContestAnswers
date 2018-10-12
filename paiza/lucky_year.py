#! python3
# coding: utf-8

M, D = input().split(' ')
a = list(map(int, input().split(' ')))
b = list(map(int, input().split(' ')))
m = list(map(int, input().split(' ')))

w, x, y, z = 0, 0, 0, 0

increment_w = lambda w: (a[0]*w+ b[0])%m[0]
increment_x = lambda x: (a[1]*x+ b[1])%m[1]
increment_y = lambda y: (a[2]*y+ b[2])%m[2]
increment_z = lambda z: (a[3]*z+ b[3])%m[3]

def judge(w, x, y, z):
    daynum = []
    if len(M) == 1: daynum.extend([0, int(M)])
    else: daynum.extend([int(M[0]), int(M[1])])
    if len(D) == 1: daynum.extend([0, int(D)])
    else: daynum.extend([int(D[0]), int(D[1])])

    random_num = [w%10, x%10, y%10, z%10]
    for rn in random_num:
        if rn in daynum: daynum.remove(rn)

    if len(daynum) == 0:
        return True
    else:
        return False

n = 0
while n <= 10000:
    if judge(w, x, y, z): break
    w = increment_w(w)
    x = increment_x(x)
    y = increment_y(y)
    z = increment_z(z)
    n += 1

print(n)
