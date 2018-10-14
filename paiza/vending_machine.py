#! python3
# coding: utf-8

import math

coins = list(map(int, input().split(' ')))
N = int(input())

for i in range(N):
    b, *nums = list(map(int, input().split(' ')))
    remain = nums[0]*500 + nums[1]*100 + nums[2]*50 + nums[3]*10 - b
    changes = [0, 0, 0, 0]
    numlist = [500, 100, 50, 10]
    if remain >= 0:
        for i in range(4):
            changes[i] = min(math.floor(remain/numlist[i]), coins[i])
            remain -= numlist[i]*changes[i]
        if remain != 0: print('impossible')
        else:
            for i in range(4):
                coins[i] -= changes[i]
            print(' '.join(list(map(str, changes))))
    else:
        print('impossible')
