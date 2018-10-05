#! python3
# distance.py

import math

x1, y1, x2, y2 = [float(x) for x in input().split(' ')]
print('%.5f'%math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2)))
