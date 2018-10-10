#! python3
# coding: utf-8

# TODO: やり直し
# 正規表現使うと結果がおかしくなる?

N = int(input())
S = list(input())

for i in range(N):
    v = input()
    si = 0
    first = 0
    for ci, c in enumerate(v):
        if c == S[si]:
            si += 1
            if si == 0:
