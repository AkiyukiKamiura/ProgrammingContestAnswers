#! python3
# reflection.py

import math

class Point():
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def projection(self, p):
        a = (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x) if self.p2.x != self.p1.x else float('inf')
        if a == 0:
            return (p.x, 2*self.p1.y - p.y)
        elif a == float('inf'):
            return (2*self.p1.x - p.x, p.y)
        else:
            b = self.p2.y - a*self.p2.x
            d = abs(-1*a*p.x + p.y - b)/math.sqrt(1 + a*a)
            ans_y = [p.y + math.sqrt(4*d*d/(a*a+1)), p.y - math.sqrt(4*d*d/(a*a+1))]
            ans_x = [p.x - a*(_y - p.y) for _y in ans_y]

            rst_x, rst_y = None, None
            tmp = abs(-1*a*ans_x[0] + ans_y[0] - b)/math.sqrt(1 + a*a) - d
            if tmp < abs(-1*a*ans_x[1] + ans_y[1] - b)/math.sqrt(1 + a*a) - d:
                rst_x, rst_y = ans_x[0], ans_y[0]
            else:
                rst_x, rst_y = ans_x[1], ans_y[1]
            return round(rst_x, 9), round(rst_y, 9)

x1, y1, x2, y2 = list(map(int, input().split(' ')))
line = Line(x1, y1, x2, y2)
q = int(input())
for i in range(q):
    x, y = list(map(int, input().split(' ')))
    p = Point(x, y)
    rst_x, rst_y = line.projection(p)
    print(rst_x, rst_y)
