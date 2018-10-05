#! python3
# allocation.py

n, k = list(map(int, input().split(' ')))
W = [int(input()) for i in range(n)]

# 最大積載量をPとした時, k台のトラックでどの荷物まで積めるのか
def check(P):
    i = 0
    for j in range(k):
        s = 0
        while s + W[i] <= P:
            s += W[i]
            i += 1
            if i == n: return n
    return i

# 2分探索する
def solve():
    left = 0
    right = 100000*10000
    mid = None
    while right - left > 1:
        mid = int((right + left)/2)
        v = check(mid)
        if v >= n:
            right = mid
        else:
            left = mid
    return right

ans = solve()
print(ans)
