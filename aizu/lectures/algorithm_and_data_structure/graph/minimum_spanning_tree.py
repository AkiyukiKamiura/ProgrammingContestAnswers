#! python3
# minimum_spanning_tree.py

# 重み付き無向グラフ
# 最小全域木はプリムのアルゴリズムで解く

from enum import Enum, auto
class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

n = int(input())
M = []
for i in range(n):
    arr = [int(x) for x in input().split(' ') if x != '']
    M.append(arr)
colors = []
d = []
p = [0 for i in range(n)]

INFTY = 2001
def prim():
    global d
    colors = [Color.WHITE for i in range(n)]
    d = [INFTY for i in range(n)]

    d[0] = 0 # iに入る辺の重み **最小全域木は (頂点の数)-1 = (辺の数)
    p[0] = -1 # 0を根にする

    while True:
        mincost = INFTY
        u = 0
        for i in range(n):
            if colors[i] != Color.BLACK and d[i] < mincost:
                mincost = d[i]
                u = i
        if mincost == INFTY: break

        colors[u] = Color.BLACK
        for v in range(n):
            if colors[v] != Color.BLACK and M[u][v] != -1:
                if M[u][v] < d[v]:
                    d[v] = M[u][v]
                    p[v] = u
                    colors[v] = Color.GRAY

prim()
print(sum(d))
