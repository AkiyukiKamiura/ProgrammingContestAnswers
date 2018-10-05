#! python3
# exhaustive_search.py

# n < 20 なので列挙しても問題ない

#MIDSTREAM
# 再帰では容量不足 -> 動的計画法で解く

n = int(input())
A = list(map(int, input().split(' ')))
q = int(input())
M = list(map(int, input().split(' ')))

# 上限と下限でフィルター
max_A = 0
min_A = float('inf')
for num in A:
    max_A += num
    if num < min_A:
        min_A = num

def rec(i, m):
    if m < 0:
        return False
    elif m == 0:
        return True
    if i >= n:
        return False

    rst = rec(i+1, m - A[i]) or rec(i+1, m)
    return rst

for m in M:
    if m < min_A or max_A < m:
        print('no')
    elif rec(0, m):
        print('yes')
    else:
        print('no')
