#! python3

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pnt):
        return math.sqrt((self.x - pnt.x)**2 + (self.y - pnt.y)**2)

class Line():
    def __init__(self, x1, y1, x2, y2):
        if x1 == x2:
            self.a = float('inf')
            self.b = None
        else:
            self.a = (y2-y1)/(x2-x1)
            self.b = y1 - self.a*x1

    def distance_from_point(self, pnt):
        if self.a == float('inf'):
            return pnt.x
        else:
            d = abs(pnt.y - self.a*pnt.x - self.b)/math.sqrt(self.a**2 + 1)
            return d

class Circle():
    def __init__(self, x, y, r):
        self.c = Point(x, y)
        self.r = r

    def cross_point_with_line(self, line):
        d = line.distance_from_point(self.c)
        perp_vec =


x, y, r = list(map(int, input().split(' ')))
cir = Circle(x, y, r)
q = int(input())
for i in range(q):
    x1, y1, x2, y2 = list(map(int, input().split(' ')))
    line = Line(x1, y1, x2, y2)
