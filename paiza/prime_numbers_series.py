#! python3
# coding: utf-8

# 本来は opts ヒープにして勝手にソートされる構造のほうが良さそう

# class Heap:


p1, p2, p3, k = list(map(int, input().split(' ')))

series = [1]
opts = []

for i in range(1, k):
    n = series[-1]
    if p1*n not in opts: opts.append(p1*n)
    if p2*n not in opts: opts.append(p2*n)
    if p3*n not in opts: opts.append(p3*n)
    min_opts = min(opts)
    series.append(min_opts)
    opts.remove(min_opts)

print(series[-1])
