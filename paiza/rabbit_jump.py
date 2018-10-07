#! python3

# TODO: やり直し

class Bushes:
    def __init__(self, N, M):
        self.bushes = [False for i in range(N)]
        self.rabbits_pos = [None for m in range(M)]
        self.num_bushes = N
        self.num_rabbits = M
        self.jumping_rabbit = 1

    def increment_rabbit(self):
        self.jumping_rabbit += 1
        if self.jumping_rabbit == self.num_rabbits + 1: self.jumping_rabbit = 1

    def next_empty_bush(self, now_bush):
        next_bush = now_bush
        while True:
            next_bush += 1
            if next_bush == self.num_bushes + 1:
                next_bush = 1
            if self.bushes[next_bush - 1] == False: break
        return next_bush

    def jump_rabbit(self):
        now_bush = self.rabbits_pos[self.jumping_rabbit - 1]
        next_empty = self.next_empty_bush(now_bush)
        self.bushes[now_bush - 1] = False
        self.bushes[next_empty - 1] = True
        self.rabbits_pos[self.jumping_rabbit - 1] = next_empty - 1

N, M, K = list(map(int, input().split(' ')))

field = Bushes(N, M)
field.rabbits_pos = [int(input())-1 for i in range(M)]
for k in range(K):
    field.jump_rabbit()
    field.increment_rabbit()

for p in field.rabbits_pos:
    output = p if p != 0 else N
    print(output)
