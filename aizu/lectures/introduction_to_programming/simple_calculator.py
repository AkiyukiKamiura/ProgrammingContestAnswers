#! python3
# simple_calculator.py

operations  = {'+': lambda a, b: a+b,
               '-': lambda a, b: a-b,
               '*': lambda a, b: a*b,
               '/': lambda a, b: int(a/b)}

while True:
    a, op, b = input().split(' ')
    if op == '?': break
    print(operations[op](int(a), int(b)))
