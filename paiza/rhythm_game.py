#! python3
# coding: utf-8

N, M = list(map(int, input().split(' ')))

combo = 0
max_combo = 0
cont_fail_flag = False
for i in range(M):
    d, p = input().split(' ')
    if '#' not in d: cont_fail_flag = False
    if not cont_fail_flag and d == p:
        combo += 1
    else:
        if '#' in d: cont_fail_flag = True
        combo = 0

    if max_combo < combo: max_combo = combo

print(max_combo)
