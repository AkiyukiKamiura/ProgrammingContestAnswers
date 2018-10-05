#! python3
# eulers_phi_function.py

import math

def eulers_phi_function(n):
    s = math.sqrt(n)
    x = n
    rst = n
    for y in range(2, math.ceil(s)):
        if x == 1: break
        while True:
            if x%y == 0:
                rst *= 1 - 1/y
                while x%y == 0:
                    x = x/y
            else:
                break
    if x > s: rst *= 1 - 1/x
    return int(rst)

n = int(input())
print(eulers_phi_function(n))
