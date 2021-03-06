#! python3
# stack.py

n, q = list(map(int, input().split(' ')))
stacks = [[] for i in range(n)]

for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        stacks[op[1]].append(op[2])
    elif op[0] == 1:
        if len(stacks[op[1]]) != 0:
            print(stacks[op[1]][-1])
    elif op[0] == 2:
        if len(stacks[op[1]]) != 0:
            stacks[op[1]].pop()
