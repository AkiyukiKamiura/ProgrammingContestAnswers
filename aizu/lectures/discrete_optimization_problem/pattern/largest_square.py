#! python3
# largest_square.py

H, W = list(map(int, input().split(' ')))
tiles = [list(map(int, input().split(' '))) for i in range(H)]

dp = [[0 for j in range(W)] for i in range(H)]
max_width = 0
for i in range(H):
    dp[i][0] = (tiles[i][0] + 1)%2
    if max_width == 0 and dp[i][0] == 1: max_width = 1
for j in range(W):
    dp[0][j] = (tiles[0][j] + 1)%2
    if max_width == 0 and dp[0][j] == 1: max_width = 1
for i in range(1, H):
    for j in range(1, W):
        if tiles[i][j] == 1:
            dp[i][j] == 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            max_width = max(max_width, dp[i][j])
print(max_width**2)
