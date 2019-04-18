# coding: utf-8

# 幅優先探索
# 上限と下限を計算する
# n日目(初日が1日目)に枝が1つ失われると, 総計で pow(2, N-n) だけ失われることになる
# 最大でパターン数は pow(2, N) <= pow(2, 35) = 3x10^10
# ダイエットしたパターン同士, しなかったパターン同士ではそれぞれ順序は保存される

import numpy as np

N, S, T = list(map(int, input().split(' ')))
day_change_amount = [list(map(int, input().split(' '))) for _ in range(N)]

pattern_count = pow(2, N)
