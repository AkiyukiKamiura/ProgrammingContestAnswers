#! python3
# single_source_shortest_path.py

# dijkstraのアルゴリズムを用いて実装

from enum import Enum, auto

INFTY = float('inf')

class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

n = int(input())
M = [[-1 for i in range(n)] for i in range(n)]
for i in range(n):
    line = list(map(int, input().split(' ')))
    if line[1] == 0: continue
    for j in range(2, 2+2*line[1], 2):
        M[i][line[j]] = line[j+1]


colors = []
d = []
p = [-1 for i in range(n)]

def dijkstra(s):
    global d
    colors = [Color.WHITE for i in range(n)]
    d = [INFTY for i in range(n)]
    d[s] = 0
    p[s] = -1

    while True:
        mincost = INFTY
        for i in range(n):
            if colors[i] != Color.BLACK and d[i] < mincost:
                mincost = d[i]
                u = i

        if mincost == INFTY: break
        colors[u] = Color.BLACK

        for v in range(n):
            if colors[v] != Color.BLACK and M[u][v] != -1:
                if d[u] + M[u][v] < d[v]:
                    d[v] = d[u] + M[u][v]
                    p[v] = u
                    colors[v] = Color.GRAY

dijkstra(0)
for i in range(n):
    print(i, d[i])
