#! python3
# breath_first_search.py

from collections import deque
from enum import Enum, auto

class Color(Enum):
    WHITE = auto()
    GRAY = auto()
    BLACK = auto()

n = int(input())
d = [0 for i in range(n)]
f = [0 for i in range(n)]

colors = [] # 頂点の訪問状態
A = [[0 for j in range(n)] for i in range(n)] # 隣接行列
queue = deque([])

# 隣接行列の初期化
for i in range(n):
    arr = list(map(int, input().split(' ')))
    u, k, v = arr[0], arr[1], arr[2:]
    for j in range(k):
        A[u-1][v[j]-1] = 1

def bfs():
    global colors, queue, d
    colors = [Color.WHITE for i in range(n)]
    d = [-1 for i in range(n)] # INF

    colors[0] = Color.GRAY
    d[0] = 0
    queue.append(0)

    while len(queue) > 0:
        u = queue.popleft()
        for v in range(n):
            if A[u][v] == 1 and colors[v] == Color.WHITE:
                colors[v] = Color.GRAY
                d[v] = d[u] + 1
                queue.append(v)
        colors[u] = Color.BLACK

bfs()

for i in range(n):
    print(i+1, d[i])
