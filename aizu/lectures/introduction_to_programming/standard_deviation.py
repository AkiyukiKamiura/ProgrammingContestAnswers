#! python3
# standard_deviation.py

import math

while True:
    n = int(input())
    if n == 0: break
    s = [int(x) for x in input().split(' ')]

    sum = 0
    for num in s:
        sum += num
    m = sum/n

    tmp_sum = 0
    for num in s:
        tmp_sum += pow(num - m, 2)

    print("%.5f"%(math.sqrt(tmp_sum/n)))
