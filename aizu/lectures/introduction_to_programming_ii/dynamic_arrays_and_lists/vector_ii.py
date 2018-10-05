#! python3
# vector_ii.py

n, q = list(map(int, input().split(' ')))
stacks = [[] for i in range(n)]

for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        stacks[op[1]].append(op[2])
    elif op[0] == 1:
        print(' '.join(list(map(str, stacks[op[1]]))))
    elif op[0] == 2:
        stacks[op[1]] = []
