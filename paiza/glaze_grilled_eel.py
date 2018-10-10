#! python3
# coding: utf-8

d, n = list(map(int, input().split(' ')))
opes = [int(input()) for i in range(n)]

# 幅優先探索 足切りが必要
states = {'R': opes[0], 'L': -opes[0]}
for i in range(1, n):
    new_states = {}
    while len(states) != 0:
        ope, val = states.popitem()
        new_ope = ope + 'R'
        new_val = val + opes[i]
        if -d <= new_val and new_val <= d:
            new_states[new_ope] = new_val
        new_ope = ope + 'L'
        new_val = val - opes[i]
        if -d <= new_val and new_val <= d:
            new_states[new_ope] = new_val
    states = new_states

print(list(states.keys())[0])
