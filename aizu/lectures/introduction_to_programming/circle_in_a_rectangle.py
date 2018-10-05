#! python3
# circle_in_a_rectangle.py

W, H, x, y, r = [int(n) for n in input().split(' ')]

if (0 <= x-r) and (x+r <= W) and (0 <= y-r) and (y+r <= H):
    print('Yes')
else:
    print('No')
