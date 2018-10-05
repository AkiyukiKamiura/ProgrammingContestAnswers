#! python3
# priority_queue.py

from heapq import heappush, heappop

n, q = list(map(int, input().split(' ')))
pqueues = [[] for i in range(n)]

for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        heappush(pqueues[op[1]], -op[2])
    elif op[0] == 1:
        if len(pqueues[op[1]]) != 0:
            print(-1*pqueues[op[1]][0])
    elif op[0] == 2:
        if len(pqueues[op[1]]) != 0:
            heappop(pqueues[op[1]])
