#! python3
# coding: utf-8

N, M = list(map(int, input().split(' ')))
events = [list(map(int, input().split(' '))) for m in range(M)]

max_earnings = 0
if N != 0 and M != 0:
    for eve in events:
        earning = sum(eve)
        if earning > 0:
            max_earnings += earning

print(max_earnings)
