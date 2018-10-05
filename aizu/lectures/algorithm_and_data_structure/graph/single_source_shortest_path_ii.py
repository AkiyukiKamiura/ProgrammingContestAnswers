#! python3
# single_source_shortest_path_ii.py

from heapq import heappush, heappop
from enum import Enum, auto

INFTY = float('inf')

class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

n = int(input())
adj_list = []
for i in range(n):
    u, k, *kv = list(map(int, input().split(' ')))
    adj_list.append(kv)

colors = []
d = []

def dijkstra(s):
    global d
    colors = [Color.WHITE for i in range(n)]
    d = [INFTY for i in range(n)]
    pque = []
    d[s] = 0

    heappush(pque, (0, s))

    while len(pque) >= 1:
        vert_u = heappop(pque)
        u = vert_u[1]
        colors[u] = Color.BLACK
        if d[u] < vert_u[0]: continue
        i = 0
        while i <= len(adj_list[u])-2:
            v = adj_list[u][i]
            if colors[v] != Color.BLACK:
                if d[u] + adj_list[u][i+1] < d[v]:
                    d[v] = d[u] + adj_list[u][i+1]
                    colors[v] = Color.GRAY
                    heappush(pque, (d[v], v))
            i += 2

dijkstra(0)
for i in range(n):
    print(i, d[i])
