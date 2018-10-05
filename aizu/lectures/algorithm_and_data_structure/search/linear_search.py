#! python3
# linear_search.py

n = int(input())
S = [int(x) for x in input().split(' ')]
q = int(input())
T = [int(x) for x in input().split(' ')]

c = 0
for t in T:
    for s in S:
        if t == s:
            c += 1
            break

print(c)
