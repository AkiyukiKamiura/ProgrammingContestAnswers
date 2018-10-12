#! python3
# coding: utf-8

N = int(input())
board = list(input())

changed = True
while changed:
    prior_color = board[0]
    prior_index = 0
    changed = False
    for i in range(1, N-1):
        if prior_index == 0 and board[i+1] != prior_color: prior_index = i
        else:
            if prior_color != board[i] and board[i+1] == prior_color:
                changed = True
                prior_color = board[i]
                board[prior_index+1:i+1] = board[i+1] * (i-prior_index)
                prior_index = i

print(board.count('b'))
