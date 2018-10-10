#! python3
# coding: utf-8

# TODO: むずかしい, やり直す

import itertools
import copy

N, M = list(map(int, input().split(' ')))
cats = [list(map(int, input().split(' '))) for i in range(N)]
cats_line = [i for i in range(N)]

# 暫定的な最小値
interim_min = 0
for i in range(N):
    for j in range(i+1):
        interim_min += cats[j][0]

state_hist = []
prior_states = [[cats_line, interim_min, 0]]
swappable = []
while prior_states != []:
    state, wait_time, discontent = prior_states.pop()
    for swap_index in swappable:
        i, j = swap_index
        if
        if state[i] < state[j] and cats[state[i]][0] < cats[state[j]][0]: continue
        if state[i] > state[j] and cats[state[i]][0] > cats[state[j]][0]: continue
        if cats[]
        new_state = copy.copy(state)
        new_state[i], new_state[j] = new_state[j], new_state[i]
        if new_state in state_hist: continue
