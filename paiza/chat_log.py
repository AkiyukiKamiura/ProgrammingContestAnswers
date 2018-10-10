#! python3
# coding: utf-8

import copy

n, g, m = list(map(int, input().split(' ')))
groups = [list(map(int, input().split(' ')))[1:] for i in range(g)]
chat_rooms = [[] for i in range(n)]

for i in range(m):
    s, c, t, msg = input().split(' ')
    s, c, t = int(s), int(c), int(t)
    if c == 0: # 社員同士
        chat_rooms[s-1].append(msg)
        chat_rooms[t-1].append(msg)
    elif c == 1: # グループに対して
        members = copy.copy(groups[t-1])
        members.append(s)
        members = list(set(members))
        for mem in members:
            chat_rooms[mem-1].append(msg)

for i, room in enumerate(chat_rooms):
    for msg in room:
        print(msg)
    if i != n-1: print('--')
