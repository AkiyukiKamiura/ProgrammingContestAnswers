#! python3
# string_search.py

# Knuth-Morris-Patt法 or Boyer-Moore法 を用いる

# 実装が簡単なのは KMP法 ？

# Boyer-Moore法
# スキップテーブルの作成法として,
# - 不一致文字規則
# - 一致サフィックス規則

# 不一致文字規則しか使用しないものとして, Boyer-Moore-Horspool法がある

def create_skip_table(pattern):
    table = [0 for i in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        if pattern[i] == pattern[j]:
            table[i] = j
            j += 1
        else:
            table[i] = j
            j = 0
    return table

def kmp_search(text, pattern):
    skip_table = create_skip_table(pattern)
    ti, pi = 0, 0
    while ti < len(text):
        # print(text)
        # print(' '*(ti-pi) + pattern)
        # print(' '*ti + '^')

        if text[ti] == pattern[pi]:
            ti += 1
            pi += 1
        elif pi == 0:
            ti += 1
        else:
            pi = skip_table[pi]
        if pi == len(pattern):
            print(ti - pi)
            pi = 0
            ti -= len(pattern)-1

text = input()
pattern = input()

kmp_search(text, pattern)
