#! python3
# prime_factorize.py

"""
手法として,
ロー法, ロー-1法, 楕円曲線法
SQUFOF, 二次ふるい, 数体ふるい
"""

import math

def simple_prime_factrize(x):
    pfs = []
    s = math.sqrt(x)
    for y in range(2, math.ceil(s)):
        if x == 1: break
        while True:
            if x%y == 0:
                pfs.append(y)
                x = x/y
            else:
                break
    if len(pfs) == 0:
        pfs.append(x)
    elif x > s:
        pfs.append(int(x))
    return pfs

n = int(input())
print(str(n) + ': ' + ' '.join([str(x) for x in simple_prime_factrize(n)]))
