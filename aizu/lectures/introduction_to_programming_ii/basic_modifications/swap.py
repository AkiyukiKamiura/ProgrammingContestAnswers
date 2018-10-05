#! python3
# swap.py

n = int(input())
a = list(map(int, input().split(' ')))
q = int(input())
for i in range(q):
    b, e, t = list(map(int, input().split(' ')))
    for k in range(e-b):
        a[b+k], a[t+k] = a[t+k], a[b+k]
print(' '.join(list(map(str, a))))
