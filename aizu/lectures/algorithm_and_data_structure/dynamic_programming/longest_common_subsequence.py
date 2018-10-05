#! python3
# longest_common_subsequence.py

def lcs(X, Y):
    global c
    m, n = len(X), len(Y)
    c = [[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
            else:
                c[i][j] = max(c[i-1][j], c[i][j-1])
    return c[m][n]

def lcs_improved(X, Y):
    hist = [0] # yの文字cまでを見た時に, hist[i]以降の文字列において, 共通文字のうち, 一番小さいindexのもの
    for c in Y:
        for i in range(len(hist)-1, -1, -1):
            next_match_i = X.find(c, hist[i])+1
            if next_match_i:
                if i+1 < len(hist):
                    hist[i+1] = min(hist[i+1], next_match_i)
                else:
                    hist.append(next_match_i)
    return len(hist)-1

q = int(input())
for i in range(q):
    X = input()
    Y = input()
    print(lcs_improved(X, Y))
