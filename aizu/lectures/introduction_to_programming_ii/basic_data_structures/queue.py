#! python3
# queue.py

from collections import deque

n, q = list(map(int, input().split(' ')))
queues = [deque([]) for i in range(n)]

for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        queues[op[1]].append(op[2])
    elif op[0] == 1:
        if len(queues[op[1]]) != 0:
            print(queues[op[1]][0])
    elif op[0] == 2:
        if len(queues[op[1]]) != 0:
            queues[op[1]].popleft()
