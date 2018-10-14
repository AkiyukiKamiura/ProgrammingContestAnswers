#! python3
# coding: utf-8

from collections import OrderedDict

N, M, T = list(map(int, input().split(' ')))
last_month_record = {}
for i in range(N):
    a, p = input().split()
    last_month_record[a] = int(p)

this_month_record = { key: 0 for key in last_month_record.keys()}
for i in range(M):
    d, w, x = input().split(' ')
    this_month_record[w] += int(x)


last_top_T = OrderedDict(sorted(last_month_record.items(), key=lambda x: (-x[1], x[0]))[:T])
top_T = OrderedDict(sorted(this_month_record.items(), key=lambda x: (-x[1], x[0]))[:T])

for i, key in enumerate(top_T.keys()):
    if key in last_top_T:
        if i < list(last_top_T.keys()).index(key):
            print(key, top_T[key], 'up')
        elif i > list(last_top_T.keys()).index(key):
            print(key, top_T[key], 'down')
        elif i == list(last_top_T.keys()).index(key):
            print(key, top_T[key], 'same')
    else:
        print(key, top_T[key], 'new')
