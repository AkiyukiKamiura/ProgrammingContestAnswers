#! python3
# disjoint_set_union_find_tree.py

class UnionFindTree():
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.find(self.par[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.par[x] = y
        else:
            self.par[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1

    def same_check(self, x, y):
        return self.find(x) == self.find(y)

n, q = [int(x) for x in input().split(' ')]
uft = UnionFindTree(n-1)

for i in range(q):
    com, x, y = [int(x) for x in input().split(' ')]
    if com == 0:
        uft.unite(x, y)
    elif com == 1:
        if uft.same_check(x, y):
            print(1)
        else:
            print(0)
