#! python3
# range_minimum_query.py

# RmQ: Range minimum Query
# Sparse Table Algorithm: 前処理 O(nlogn), クエリ時間 O(1)
# Segment Tree のデータ構造を使って実装可能
# - 初期化: 子ノードから順に再帰的に O(n)

import math

INIT_VAL = pow(2, 31)-1

class SegmentTree():
    def __init__(self, n):
        self.n = n
        self.height = math.ceil(math.log2(n))
        self.nodes = [INIT_VAL for i in range(pow(2, self.height+1)-1)]
        self.leaf_start = pow(2, self.height)-1

    def update(self, i, x):
        pntr = self.leaf_start + i
        self.nodes[pntr] = x
        while True:
            pntr = (pntr-1)//2
            if pntr == -1: break
            l, r = pntr*2 + 1, pntr*2 + 2
            self.nodes[pntr] = min(self.nodes[l], self.nodes[r])

    def __query(self, s, t, k, l, r):
        if t - s <= 0: return INIT_VAL
        if r <= s or t <= l: return INIT_VAL
        if l == s and t == r: return self.nodes[k]
        else:
            m = (l+r)//2
            if t <= m:
                return self.__query(s, t, k*2+1, l, m)
            elif m <= s:
                return self.__query(s, t, k*2+2, m, r)
            else:
                vl = self.__query(s, m, k*2+1, l, m)
                vr = self.__query(m, t, k*2+2, m, r)
                return min(vl, vr)

    def find(self, s, t):
        return self.__query(s, t+1, 0, 0, pow(2, self.height))

n, q = list(map(int, input().split(' ')))
st = SegmentTree(n)
for i in range(q):
    com, x, y = list(map(int, input().split(' ')))
    if com == 0:
        st.update(x, y)
    elif com == 1:
        print(st.find(x, y))
