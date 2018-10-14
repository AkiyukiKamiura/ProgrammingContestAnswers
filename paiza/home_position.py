#! python3
# coding: utf-8

import numpy as np

alphabets = list('qwertyuiopasdfghjklzxcvbnm')
keyboards = {}
row = 0
col = 0
for al in alphabets:
    if al == 'a' or al == 'z':
        row += 1
        col = 0
    keyboards[al] = np.array([row, col])
    col += 1

S = input()
count = 0
prior_hand = (keyboards[S[0]][1]-4.5)/abs(keyboards[S[0]][1]-4.5)
for i in range(1, len(S)):
    prior_key_pos = keyboards[S[i-1]]
    now_key_pos = keyboards[S[i]]
    diff = now_key_pos - prior_key_pos
    if 0 in diff and abs(diff[0] - diff[1]) <= 1:
        if (now_key_pos[1]-4.5)*prior_hand < 0:
            count += 1
    else:
        prior_hand = (now_key_pos[1]-4.5)/abs(now_key_pos[1]-4.5)

print(count)
