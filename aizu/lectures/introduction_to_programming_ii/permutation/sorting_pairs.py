#! python3
# sorting_pairs.py

n = int(input())
points = []
for i in range(n):
    x, y = list(map(int, input().split(' ')))
    points.append([x, y])

points = sorted(points, key=lambda x: x[1])
points = sorted(points, key=lambda x: x[0])

for x, y in points:
    print(x, y)
