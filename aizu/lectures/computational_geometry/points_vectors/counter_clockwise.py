#! python3
# counter_clockwise.py

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Vector():
    def __init__(self, start, end):
        self.x = end.x - start.x
        self.y = end.y - start.y
        self.r = math.sqrt(pow(self.x, 2) + pow(self.y, 2))
        self.theta = math.atan2(self.y, self.x)

x0, y0, x1, y1 = list(map(int, input().split(' ')))
p0, p1 = Point(x0, y0), Point(x1, y1)
vec1 = Vector(p0, p1)

q = int(input())
for i in range(q):
    x2, y2 = list(map(int, input().split(' ')))
    p2 = Point(x2, y2)
    vec2 = Vector(p0, p2)
    if vec2.r == 0:
        print('ON_SEGMENT')
    elif vec1.theta == vec2.theta:
        if vec1.r < vec2.r:
            print('ONLINE_FRONT')
        else:
            print('ON_SEGMENT')
    elif abs(vec1.theta - vec2.theta) == math.pi:
        print('ONLINE_BACK')
    elif (0 < vec2.theta - vec1.theta and vec2.theta - vec1.theta < math.pi)  or vec2.theta - vec1.theta < -1*math.pi:
        print('COUNTER_CLOCKWISE')
    elif (-1*math.pi < vec2.theta - vec1.theta and vec2.theta - vec1.theta < 0) or vec2.theta - vec1.theta > math.pi:
        print('CLOCKWISE')
