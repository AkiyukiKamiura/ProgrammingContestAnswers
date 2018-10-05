#! python3
# equal_range.py

import bisect

n = int(input())
a = list(map(int, input().split(' ')))
q = int(input())
for i in range(q):
    k = int(input())
    print(bisect.bisect_left(a, k), bisect.bisect_right(a, k))
