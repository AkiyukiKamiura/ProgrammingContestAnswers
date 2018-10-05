#! python3
# deque.py

from collections import deque

deq = deque([])

q = int(input())
for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        if op[1] == 0:
            deq.appendleft(op[2])
        else:
            deq.append(op[2])
    elif op[0] == 1:
        print(deq[op[1]])
    elif op[0] == 2:
        if op[1] == 0:
            deq.popleft()
        else:
            deq.pop()
