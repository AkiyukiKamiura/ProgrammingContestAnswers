#! python3
# polygon_point_containment.py

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, pnt):
        if self.x == pnt.x and self.y == pnt.y: return True
        return False

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def inner_product(self, vec):
        return self.x*vec.x + self.y*vec.y

    def outer_product(self, vec):
        return self.x*vec.y - self.y*vec.x

    def norm(self):
        return math.sqrt(self.x**2 + self.y**2)

    def polar(self):
        r = self.norm()
        theta = math.atan2(self.y, self.x)
        return r, theta


class Segment():
    def __init__(self, p1=None, p2=None):
        self.p1 = p1
        self.p2 = p2

    def is_intersect(self, seg):
        a = (seg.p1.x - seg.p2.x) * (self.p1.y - seg.p1.y) + (seg.p1.y - seg.p2.y) * (seg.p1.x - self.p1.x)
        b = (seg.p1.x - seg.p2.x) * (self.p2.y - seg.p1.y) + (seg.p1.y - seg.p2.y) * (seg.p1.x - self.p2.x)
        c = (self.p1.x - self.p2.x) * (seg.p1.y - self.p1.y) + (self.p1.y - self.p2.y) * (self.p1.x - seg.p1.x)
        d = (self.p1.x - self.p2.x) * (seg.p2.y - self.p1.y) + (self.p1.y - self.p2.y) * (self.p1.x - seg.p2.x)
        e = (self.p1.x - seg.p1.x)*(self.p2.x - seg.p2.x)
        f = (self.p1.x - seg.p2.x)*(self.p2.x - seg.p1.x)
        g = (self.p1.y - seg.p1.y)*(self.p2.y - seg.p2.y)
        h = (self.p1.y - seg.p2.y)*(self.p2.y - seg.p1.y)
        return a*b <= 0 and c*d <= 0 and (e <= 0 or f <= 0) and (g <= 0 or h <= 0)

    def on_segment(self, pnt):
        if self.p1 == pnt or self.p2 == pnt:
            return True
        a, b = Vector(self.p2.x - self.p1.x, self.p2.y - self.p1.y), Vector(pnt.x - self.p1.x, pnt.y - self.p1.y)
        a_r, a_theta = a.polar()
        b_r, b_theta = b.polar()
        if a_theta == b_theta:
            if 0 < b_r/a_r and b_r/a_r < 1:
                return True
        return False

n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    points.append(Point(x, y))
points.append(points[0])
segments = [Segment(points[i], points[i+1]) for i in range(n)]

q = int(input())
for i in range(q):
    x, y = list(map(int, input().split(' ')))
    right, left = Segment(Point(x, y), Point(10001, y)), Segment(Point(x, y), Point(-10001, y))
    up, down = Segment(Point(x, y), Point(x, 10001)), Segment(Point(x, y), Point(x, -10001))
    r_int, l_int, u_int, d_int = 0, 0, 0, 0
    on_segment = False
    for seg in segments:
        if seg.on_segment(Point(x, y)):
            on_segment = True
            break
        if seg.is_intersect(right): r_int += 1
        if seg.is_intersect(left): l_int += 1
        if seg.is_intersect(up): u_int += 1
        if seg.is_intersect(down): d_int += 1

    for pnt in points[:n]:
        if right.on_segment(pnt): r_int -= 1
        if left.on_segment(pnt): l_int -= 1
        if up.on_segment(pnt): u_int -= 1
        if down.on_segment(pnt): d_int -= 1

    if on_segment:
        print(1)
    elif (r_int%2 == 1 or l_int%2 == 1) and (u_int%2 == 1 or d_int%2 == 1):
        print(2)
    else:
        print(0)
