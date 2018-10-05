#! python3
# queue.py

from collections import deque

n, q = [int(x) for x in input().split(' ')]

queue = deque([])
for i in range(n):
    inp = input().split(' ')
    queue.append([inp[0], int(inp[1])])

elapsed_time = 0
while len(queue) > 0:
    proc = queue.popleft()
    if proc[1] - q <= 0:
        elapsed_time += proc[1]
        print(proc[0], elapsed_time)
    else:
        elapsed_time += q
        queue.append([proc[0], proc[1] - q])
