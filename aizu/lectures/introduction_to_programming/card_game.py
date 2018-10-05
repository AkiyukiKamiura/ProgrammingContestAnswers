#! python3
# card_game.py

n = int(input())
turns = [input() for i in range(n)]

taro, hanako = 0, 0
for turn in turns:
    t, h = turn.split(' ')
    min_len = len(t) if len(t) <= len(h) else len(h)

    win_flag = 0 # -1: taro, 1: hanako, 0: draw
    for i in range(min_len):
        if ord(t[i]) < ord(h[i]):
            win_flag = 1
            break
        elif ord(h[i]) < ord(t[i]):
            win_flag = -1
            break

    if win_flag == 0:
        if len(t) < len(h):
            win_flag = 1
        elif len(h) < len(t):
            win_flag = -1

    if win_flag == -1:
        taro += 3
    elif win_flag == 1:
        hanako += 3
    else:
        taro += 1
        hanako += 1

print(taro, hanako)
