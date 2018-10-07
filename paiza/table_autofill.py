#! python3

H, W = list(map(int, input().split(' ')))
table = [[None for w in range(W)] for h in range(H)]
table[0][:2] = list(map(int, input().split(' ')))
table[1][:2] = list(map(int, input().split(' ')))

vert_diff_1 = table[1][0] - table[0][0]
vert_diff_2 = table[1][1] - table[0][1]
horiz_diff_1 = table[0][1] - table[0][0]
horiz_diff_2 = table[1][1] - table[1][0]

for h in range(1, H):
    table[h][0] = table[h-1][0] + vert_diff_1
    table[h][1] = table[h-1][1] + vert_diff_2

for w in range(1, W):
    table[0][w] = table[0][w-1] + horiz_diff_1
    table[1][w] = table[1][w-1] + horiz_diff_2

for h in range(2, H):
    for w in range(2, W):
        horiz_diff_w = table[h][1] - table[h][0]
        table[h][w] = table[h][w-1] + horiz_diff_w

for row in table:
    print(' '.join(list(map(str, row))))
