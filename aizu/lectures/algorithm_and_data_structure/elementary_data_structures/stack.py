#! python3
# stack.py

symbols = input().split(' ')
stack = []

def calc(op):
    global stack
    if op == '+':
        return stack.pop()+stack.pop()
    elif op == '-':
        return -1 * stack.pop()+stack.pop()
    elif op == '*':
        return stack.pop()*stack.pop()

for s in symbols:
    if s in ['+', '-', '*']:
        stack.append(calc(s))
    else:
        stack.append(int(s))

print(stack.pop())
