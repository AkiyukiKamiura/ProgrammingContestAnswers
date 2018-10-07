#! python3
# coding: utf-8

N = int(input())
rst = ''
for n in range(N):
    inp = input()
    added = False
    for i in range(len(inp), 0, -1):
        if rst.endswith(inp[:i]):
            rst += inp[i:]
            added = True
            break
    if not added:
        rst += inp
print(rst)
