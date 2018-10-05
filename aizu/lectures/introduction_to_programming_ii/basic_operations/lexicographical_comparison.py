#! python3
# lexicographical_comparison.py

n = int(input())
a = list(map(int, input().split(' ')))
m = int(input())
b = list(map(int, input().split(' ')))

rst = None

loop_num = n if n <= m else m
for i in range(loop_num):
    if a[i] < b[i]:
        rst = 1
    elif a[i] > b[i]:
        rst = 0
    if rst != None: break

if rst == None:
    if len(a) < len(b):
        rst = 1
    else:
        rst = 0

print(rst)
