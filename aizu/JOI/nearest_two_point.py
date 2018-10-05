#! python3

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self, pnt):
        return (pnt.x - self.x)**2 + (pnt.y - self.y)**2

n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    points.append(Point(x, y))

min_dist = float('inf')
for i in range(n-1):
    for j in range(i+1, n):
        dist = points[i].norm(points[j])
        if min_dist > dist:
            min_dist = dist

print(dist)
