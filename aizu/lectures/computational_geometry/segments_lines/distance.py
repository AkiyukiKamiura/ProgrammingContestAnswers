#! python3
# distance.py

import math

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, pnt):
        return math.sqrt((self.x - pnt.x)**2 + (self.y - pnt.y)**2)

class Segment():
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)
        if self.p1.x == self.p2.x:
            self.a = float('inf')
            self.b = None
        else:
            self.a = (self.p1.y - self.p2.y)/(self.p1.x - self.p2.x)
            self.b = self.p1.y - self.a*self.p1.x

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

    def cross_point(self, seg):
        if self.is_intersect(seg) == False: return None
        if self.a == float('inf'):
            return self.p1.x, seg.a * self.p1.x + seg.b
        elif seg.a == float('inf'):
            return seg.p1.x, self.a * seg.p1.x + self.b
        else:
            x = -(self.b - seg.b)/(self.a - seg.a)
            y = seg.a * x + seg.b
            return x, y

    def distance_with_point(self, pnt):
        vec_a = Point(self.p2.x - self.p1.x, self.p2.y - self.p1.y)
        vec_b = Point(pnt.x - self.p1.x, pnt.y - self.p1.y)
        ip = vec_a.x*vec_b.x + vec_a.y*vec_b.y
        dist2 = (self.p1.x - self.p2.x)**2 + (self.p1.y - self.p2.y)**2
        if ip/dist2 <= 0:
            return pnt.distance(self.p1)
        elif ip/dist2 >= 1:
            return pnt.distance(self.p2)
        else:
            tmppnt = Point(self.p1.x + vec_a.x*(ip/dist2), self.p1.y + vec_a.y*(ip/dist2))
            return pnt.distance(tmppnt)

    def distance_as_line(self, pnt):
        if self.a == float('inf'): return abs(pnt.x - self.p1.x)
        return abs(pnt.y - self.a*pnt.x - self.b)/math.sqrt(1 + self.a**2)

    def distance_with_segment(self, seg):
        if self.is_intersect(seg): return 0
        a = self.distance_with_point(seg.p1)
        b = self.distance_with_point(seg.p2)
        c = seg.distance_with_point(self.p1)
        d = seg.distance_with_point(self.p2)
        return min(a, b, c, d)

q = int(input())
for i in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = list(map(int, input().split(' ')))
    line1, line2 = Segment(x0, y0, x1, y1), Segment(x2, y2, x3, y3)
    dist = line1.distance_with_segment(line2)
    print('%.9f'%dist)
