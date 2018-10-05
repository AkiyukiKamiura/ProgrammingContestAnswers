#! python3

# 分枝限定法で解いてみる
# 暫定解 < 部分問題の最適解ならば、探索を中止
# 0-1ナップサック問題の緩和問題を解き、求められる解を暫定解とする

n, w = list(map(int, input().split(' ')))
items = [list(map(int, input().split(' '))) for i in range(n)]
