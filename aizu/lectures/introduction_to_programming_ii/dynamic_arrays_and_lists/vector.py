#! python3
# vector.py

stack = []

q = int(input())
for i in range(q):
    op = list(map(int, input().split(' ')))
    if op[0] == 0:
        stack.append(op[1])
    elif op[0] == 1:
        print(stack[op[1]])
    elif op[0] == 2:
        stack.pop()
