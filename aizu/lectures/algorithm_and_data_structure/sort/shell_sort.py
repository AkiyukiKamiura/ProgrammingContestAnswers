#! python
# shell_sort.py

import math
import sys

count = 0
m = 0
G = []

def insertion_sort(A, N, g):
    global count
    for i in range(g, N):
        v = A[i]
        j = i - g
        while j >= 0 and A[j] > v:
            A[j+g] = A[j]
            j = j - g
            count += 1
        A[j + g] = v

# h_(i+1) = 3h_i + 1 が最良の間隔 (らしい)
def shell_sort(A, N):
    global m, G
    m = math.floor(math.log(2*N+1, 3))
    G = [int((pow(3, i)-1)/2) for i in range(m, 0, -1)]

    for i in range(m):
        insertion_sort(A, N, G[i])


n = int(input())
A = list(map(int, sys.stdin.readlines()))
shell_sort(A, n)

print(m)
print(' '.join([str(h) for h in G]))
print(count)
for x in A:
    print(x)
