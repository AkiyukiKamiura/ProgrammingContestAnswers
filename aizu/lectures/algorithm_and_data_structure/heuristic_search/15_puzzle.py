#! python3
# 15_puzzle.py

# 反復深化探索を用いる
# 反復深化 - IDA*(反復深化A*): 推定値を用いて枝を刈るアルゴリズム (推定値例: マンハッタン距離)
#          - A*: [始点から現在位置までのコスト + ゴールまでの推定値] が最も小さいものから探索

# 与えられたパズルは45手以内で解くことができるという成約があるため, 反復深化でも有効: 最大で4^45(バックトラックで16!通り)
# 今回はA*を使って解く

import heapq, copy

N, N2 = 4, 16
dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
dir = ['r', 'u', 'l', 'd']
MDT = [[abs(i//N - j//N) + abs(i%N - j%N) for j in range(N2)] for i in range(N2)]

class Puzzle:
    def __init__(self, field=None, space=None, MD=None, cost=None):
        self.field = field
        self.space = space
        self.MD = MD
        self.cost = cost

    def __lt__(self, pzl): # <
        for i in range(N2):
            if self.field[i] == pzl.field[i]:
                continue
            return self.field[i] > pzl.field[i]
        return False

    def set_MD(self):
        sum = 0
        for i in range(N2):
            if self.field[i] == N2: continue
            sum += MDT[i][self.field[i]-1]
        self.MD = sum

class State():
    def __init__(self, pzl=None, estimated=None):
        self.puzzle = pzl
        self.estimated = estimated

    def __lt__(self, stat):
        return self.estimated < stat.estimated

def astar(pzl):
    pqueue = []
    pzl.set_MD()
    pzl.cost = 0
    V = {}
    u, v = Puzzle(), Puzzle()
    initial = State(pzl, pzl.MD)
    heapq.heappush(pqueue, initial)

    if pzl.MD == 0: return pzl.cost

    while len(pqueue) != 0:
        st = heapq.heappop(pqueue)
        u = st.puzzle

        V[str(u.field)] = True

        sx = u.space//N
        sy = u.space%N
        for r in range(4):
            tx, ty = sx + dx[r], sy + dy[r]
            if tx < 0 or ty < 0 or tx >= N or ty >= N: continue
            v = Puzzle(field=copy.copy(u.field), space=u.space, MD=u.MD, cost=u.cost)

            v.MD -= MDT[tx*N + ty][v.field[tx*N + ty]-1]
            v.MD += MDT[sx*N + sy][v.field[tx*N + ty]-1]

            v.field[sx*N + sy], v.field[tx*N + ty] = v.field[tx*N + ty], v.field[sx*N + sy]
            v.space = tx*N + ty
            if not V.get(str(v.field)):
                v.cost += 1
                if v.MD == 0: return v.cost
                news = State()
                news.puzzle = v
                news.estimated = v.cost + v.MD
                heapq.heappush(pqueue, news)
    return -1

field = []
for i in range(4):
    field.extend(list(map(int, input().split(' '))))

space = None
for i in range(N2):
    if field[i] == 0:
        field[i] = N2
        space = i
        break

s = Puzzle(field=field, space=space)
print(astar(s))
