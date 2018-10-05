#! python3
# connected_components.py

# 連結成分分解
# 辺の数が少ない疎なグラフでは, 隣接リストでの表現が効率いい
# 隣接リストを幅優先探索

from collections import deque
import sys
sys.setrecursionlimit(100000)

n, m = list(map(int, input().split(' ')))
adj_list = [[] for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().split(' ')))
    adj_list[u].append(v)
    adj_list[v].append(u)

# 深さ優先
# 全ての点をたどって連結しているもの同士を同じ色に設定する
colors = []

def adj_dfs(r, c):
    global colors
    stack = deque([])
    stack.append(r)
    colors[r] = c
    while len(stack) != 0:
        u = stack.pop()
        for v in adj_list[u]:
            if colors[v] == None:
                colors[v] = c
                stack.append(v)

def assign_color():
    global colors
    id = 1
    colors = [None for i in range(n)]
    for u in range(n):
        if colors[u] == None:
            id += 1
            adj_dfs(u, id)

assign_color()

q = int(input())
for i in range(q):
    s, e = list(map(int, input().split(' ')))
    if colors[s] == colors[e]:
        print('yes')
    else:
        print('no')
