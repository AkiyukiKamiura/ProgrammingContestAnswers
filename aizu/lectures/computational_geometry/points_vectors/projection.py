#! python3
# projection.py

import math

class Point():
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.abs = math.sqrt(x*x + y*y)

    def constant_multipled(self, c):
        return Vector(self.x*c, self.y*c)

    def inner_product(self, vec):
        return self.x*vec.x + self.y*vec.y

x1, y1, x2, y2 = list(map(int, input().split(' ')))
start = Point(x1, y1)
base_vec = Vector(x2-x1, y2-y1)
q = int(input())
vectors = []
for i in range(q):
    x, y = list(map(int, input().split(' ')))
    vectors.append(Vector(x-start.x, y-start.y))

for vec in vectors:
    if vec.abs == 0:
        ans_x, ans_y = 0, 0
        print('%.8f'%ans_x, '%.8f'%ans_y)
        continue
    cos = base_vec.inner_product(vec)/(base_vec.abs*vec.abs)
    b_cos = vec.abs*cos
    vec_x = base_vec.constant_multipled(b_cos/base_vec.abs)
    ans_x, ans_y = vec_x.x + start.x, vec_x.y + start.y
    print('%.8f'%ans_x, '%.8f'%ans_y)
