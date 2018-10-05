#! python3
# triangle.py

import math

a, b, C = [int(x) for x in input().split(' ')]

S = a * b * math.sin(math.radians(C)) / 2.0
L = a + b + math.sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(math.radians(C)))
h = b * math.sin(math.radians(C))

print('%.5f'%S)
print('%.5f'%L)
print('%.5f'%h)
