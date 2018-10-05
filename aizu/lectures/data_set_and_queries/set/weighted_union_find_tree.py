#! python3
# weighted_union_find_tree.py

class WeightedUnionFindTree():
    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.weight = [0] * (n+1)

    def find(self, x):
        if self.par[x] == x:
            return x
        else:
            y = self.find(self.par[x])
            self.weight[x] += self.weight[self.par[x]]
            self.par[x] = y
            return y

    def unite(self, x, y, w):
        rx = self.find(x)
        ry = self.find(y)
        if self.rank[rx] < self.rank[ry]:
            self.par[rx] = ry
            self.weight[rx] = w - self.weight[x] + self.weight[y]
        else:
            self.par[ry] = rx
            self.weight[ry] = -w - self.weight[y] + self.weight[x]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def diff(self, x, y):
        return self.weight[x] - self.weight[y]

n, q = [int(x) for x in input().split(' ')]
wuft = WeightedUnionFindTree(n-1)
for i in range(q):
    query = [int(x) for x in input().split(' ')]
    if query[0] == 0:
        x, y, z = query[1:]
        wuft.unite(x, y, z)
    elif query[0] == 1:
        x, y = query[1:]
        if wuft.same(x, y):
            print(wuft.diff(x,y))
        else:
            print('?')
