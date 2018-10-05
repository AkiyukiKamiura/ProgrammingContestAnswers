#! python3

import sys

def triangle_check(a, b, c):
    e1, e2, e3 = sorted([a, b, c], reverse=True)
    if e1 <= 0 or e2 <= 0 or e3 <= 0: return 0
    if e1 > e2 + e3: return 0
    if e1**2 == e2**2 + e3**2: return 1
    elif e1**2 < e2**2 + e3**2: return 2
    elif e1**2 > e2**2 + e3**2: return 3

ans = [0 for i in range(4)]

lines = sys.stdin.readlines()
for line in lines:
    a, b, c = list(map(int, line.split(' ')))
    rst = triangle_check(a, b, c)
    if rst == 0:
        print(' '.join(list(map(str, ans))))
        break
    ans[0] += 1
    ans[rst] += 1
