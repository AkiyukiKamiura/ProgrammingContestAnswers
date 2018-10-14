#! python3
# coding: utf-8

import itertools

N, K = list(map(int, input().split(' ')))
items = list(range(1, 2*N+1))

if K < N:
    print(0)
else:
    combi = list(itertools.combinations(items, N))
    ans = 0
    for a_item in combi:
        b_item = []
        for i in range(1, 2*N+1):
            if i not in a_item: b_item.append(i)

        val = 0
        for i in range(N):
            val += abs(a_item[i] - b_item[i])

        if val <= K:
            ans += 1
            
    print(ans)
