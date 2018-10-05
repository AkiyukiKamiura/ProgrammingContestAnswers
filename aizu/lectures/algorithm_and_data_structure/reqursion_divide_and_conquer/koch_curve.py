#! python3
# koch_curve.py

import math

def rotate(x, y, theta):
    return (round(x*math.cos(theta) -1*y*math.sin(theta), 5), round(x*math.sin(theta) + y*math.cos(theta), 5))

def koch(p1, p2, n):
    s = (round((2*p1[0] + p2[0])/3, 5), round((2*p1[1] + p2[1])/3, 5))
    t = (round((p1[0] + 2*p2[0])/3, 5), round((p1[1] + 2*p2[1])/3, 5))
    rotated = rotate(t[0]-s[0], t[1]-s[1], math.pi/3)
    u = (s[0] + rotated[0], s[1] + rotated[1])

    if n == 0:
        print(round(p1[0], 5), round(p1[1], 5))
    elif n == -1:
        return None

    koch(p1, s, n-1)
    koch(s, u, n-1)
    koch(u, t, n-1)
    koch(t, p2, n-1)

n = int(input())
koch((0.0, 0.0), (100, 0.0), n)
print(100, 0.0)
