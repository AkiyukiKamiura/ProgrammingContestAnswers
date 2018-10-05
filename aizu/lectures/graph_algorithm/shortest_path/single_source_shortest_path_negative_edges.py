#! python3
# single_source_shortest_path_negative_edges.py

# 採用アルゴリズム
# ベルマンフォード法
# O(E*V) < O(E*logV): ダイクストラ法
# 動的計画法

d = []          # コスト distance

# input
V, E, r = list(map(int, input().split(' ')))
edges = [list(map(int, input().split(' '))) for i in range(E)]

def bellman_ford(s):
    global d
    d = [float('inf') for i in range(V)]
    d[s] = 0

    for i in range(V-1):
        for s, t, w in edges:
            if d[t] > d[s] + w:
                d[t] = d[s] + w

    for s, t, w in edges:
        if d[s] + w < d[t]: return False
    return True

if bellman_ford(r):
    for w in d:
        if w == float('inf'):
            print('INF')
        else:
            print(w)
else:
    print('NEGATIVE CYCLE')
