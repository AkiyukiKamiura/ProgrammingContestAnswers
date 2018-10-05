#! python3
# depth_first_search.py

from enum import Enum, auto

class Color(Enum):
    WHITE = auto() # 未訪問の頂点
    GRAY = auto() # 訪問済みだが, 全ての接点の調査は済んでいない状態の接点
    BLACK = auto() # 訪問, 調査済みの接点

n = int(input())
d = [0 for i in range(n)]
f = [0 for i in range(n)]

colors = [] # 頂点の訪問状態
A = [[0 for j in range(n)] for i in range(n)] # 隣接行列
# stack = [] ## スタックによる実装では頂点の保持が必要 => 再帰によって実装

# 隣接行列の初期化
for i in range(n):
    arr = list(map(int, input().split(' ')))
    u, k, v = arr[0], arr[1], arr[2:]
    for j in range(k):
        A[u-1][v[j]-1] = 1

time = 0
def dfs_init():
    global colors
    colors = [Color.WHITE for i in range(n)]
    dfs(0)

def dfs(u):
    global time
    colors[u] = Color.GRAY
    time += 1
    d[u] = time
    for v in range(n):
        if A[u][v] == 1 and colors[v] == Color.WHITE:
            dfs(v)
    colors[u] = Color.BLACK
    time += 1
    f[u] = time

dfs_init()
for u in range(n):
    if colors[u] == Color.WHITE:
        dfs(u)

# 出力
for i in range(n):
    print(i+1, d[i], f[i])
