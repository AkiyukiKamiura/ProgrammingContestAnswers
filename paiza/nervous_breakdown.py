#! python3

H, W, N = list(map(int, input().split(' ')))
cards = [list(map(int, input().split(' '))) for h in range(H)]

player_cards = [0 for i in range(N)]
now_player = 0

L = int(input())
for l in range(L):
    a, b, A, B = list(map(int, input().split(' ')))
    if cards[a-1][b-1] == cards[A-1][B-1]:
        player_cards[now_player] += 2
    else:
        now_player += 1
        if now_player == N: now_player = 0

for c in player_cards:
    print(c)
