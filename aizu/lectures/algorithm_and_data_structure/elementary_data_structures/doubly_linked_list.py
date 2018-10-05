#! python3
# doubly_linked_list.py

from collections import deque

keys = deque([])

n = int(input())

for i in range(n):
    command = input()
    if command == 'deleteFirst':
        keys.popleft()
    elif command == 'deleteLast':
        keys.pop()
    else:
        command, x = command.split(' ')
        if command == 'insert':
            keys.appendleft(int(x))
        elif command == 'delete':
            if int(x) in keys:
                keys.remove(int(x))

print(' '.join([str(k) for k in keys]))
