#! python3
# minimum_cost_sort.py

def solve(A, n, s):
    ans = 0

    V = [False for i in range(n)] # 値が交換済みかどうか
    B = sorted(A)
    T = [None for i in range(10001)]
    for i in range(n):
        T[B[i]] = i

    for i in range(n):
        if V[i]: continue
        cur = i # カーソル(サークル内で動かす)
        S = 0 # サークル内の数字の総和
        m = 10000
        an = 0 # サークルに含まれる数字の数
        while True:
            V[cur] = True
            an += 1
            v = A[cur]
            m = min(m, v) # mがサークル内の数字の最小値
            S += v
            cur = T[v]
            if V[cur]: break
        ans += min(S + (an-2)*m, m+S+(an+1)*s)

    return ans

n = int(input())
A = list(map(int, input().split(' ')))
s = min(A)
ans = solve(A, n, s)
print(ans)
