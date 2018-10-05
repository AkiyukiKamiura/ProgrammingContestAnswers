#! python3
# parallel_orthogonal.py

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line():
    def __init__(self, x1, y1, x2, y2):
        self.p1 = Point(x1, y1)
        self.p2 = Point(x2, y2)

    def get_slope(self):
        if self.p1.x == self.p2.x:
            return float('inf')
        return (self.p2.y - self.p1.y)/(self.p2.x - self.p1.x)

q = int(input())
for i in range(q):
    x0, y0, x1, y1, x2, y2, x3, y3 = list(map(int, input().split(' ')))
    line1, line2 = Line(x0, y0, x1, y1), Line(x2, y2, x3, y3)
    a1, a2 = line1.get_slope(), line2.get_slope()
    if a1 == a2: # 平行
        print('2')
    elif round(a1*a2, 8) == -1.0:
        print('1')
    elif (a1 == float('inf') and a2 == 0) or (a1 == 0 and a2 == float('inf')):
        print('1')
    else:
        print('0')
