#! python3
# coding: utf-8

import copy

S = int(input()) # 福袋に詰める商品の価値の合計の最小値
N = int(input()) # 福袋に詰める候補となる商品の数
values = [int(input()) for i in range(N)] # 福袋に詰める候補となる商品の価値
values = sorted(values, reverse=True)

# 深さ優先探索はどうだろうか
# パターン数 2の10乗 = 1024
combination_num = 0
def depth_first_search(bag_sum, current_depth):
    global combination_num

    if bag_sum >= S or current_depth >= N: return False
    if bag_sum + values[current_depth] >= S: combination_num += 1

    depth_first_search(bag_sum + values[current_depth], current_depth+1) # 新しい要素を含むパターン
    depth_first_search(bag_sum, current_depth+1)                         # 新しい要素を含まないパターン

depth_first_search(0, 0)
print(combination_num)
