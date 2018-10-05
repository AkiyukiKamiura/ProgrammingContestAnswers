#! python3
# all_shortest_path.py

# 採用アルゴリズム
# ワーシャルフロイドのアルゴリズム
# 実装はめっちゃ簡単だけど, O(V**3)
# 動的計画法

V, E = list(map(int, input().split(' ')))
A = [[float('inf') if i != j else 0 for i in range(V)] for j in range(V)]
for i in range(E):
    s, t, d = list(map(int, input().split(' ')))
    A[s][t] = d

def warchall_floyd():
    global A
    for k in range(V):
        for i in range(V):
            if A[i][k] == float('inf'): continue
            for j in range(V):
                if A[k][j] == float('inf'): continue
                A[i][j] = min(A[i][j], A[i][k] + A[k][j])
                if i == j and A[i][i] < 0: return False
    return True

if warchall_floyd():
    for i in range(V):
        print(' '.join([str(x) if x != float('inf') else 'INF' for x in A[i]]))
else:
    print('NEGATIVE CYCLE')
