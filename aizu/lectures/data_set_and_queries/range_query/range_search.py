#! python3
# range_search.py

# kd tree
#

class KDTreeNode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.

class KDTree:
    def __init__(self, xs, ys):


# 入力
n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    points.append(Point(x, y))
q = int(input())
for i in range(q):
    sx, tx, sy, ty = list(map(int, input().split(' ')))
