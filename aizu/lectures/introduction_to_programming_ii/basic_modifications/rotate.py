#! python3
# rotate.py

dist = lambda b, e, k: (k+(e-m))%(e-b)

n = int(input())
a = list(map(int, input().split(' ')))
q = int(input())
for i in range(q):
    b, m, e = list(map(int, input().split(' ')))

    tmp = [None for i in range(e-b)]
    for k in range(e-b):
        tmp[dist(b, e, k)] = a[b+k]
    a[b:e] = tmp

print(' '.join(list(map(str, a))))
