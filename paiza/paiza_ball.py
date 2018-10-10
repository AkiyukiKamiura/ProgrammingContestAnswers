#! python3
# coding: utf-8

a, b, n = list(map(int, input().split(' ')))
pins = [int(x) if x != 'G' else 0 for x in input().split(' ')]
turns = [[] for i in range(a)]
turn = 0
hand = 0
for pin in pins:
    turns[turn].append(pin)
    hand += 1
    if turn != a-1:
        if hand == 2 or pin == b:
            turn += 1
            hand = 0

turn_scores = [0 for i in range(a)]
last_turn = turns[-1]
if len(last_turn) == 2:
    turn_scores[-1] = last_turn[0] + last_turn[1]
elif last_turn[0] + last_turn[1] == b and last_turn[1] >= 1:
    turn_scores[-1] = last_turn[0] + last_turn[1] + 2*last_turn[2]
else:
    score = sum(last_turn)
    if last_turn[1] == b: score += last_turn[2]
    if last_turn[0] == b: score += last_turn[1] + last_turn[2]
    turn_scores[-1] = score

for i in range(a-2, -1, -1):
    if turns[i][0] == b:
        if len(turns[i+1]) == 1: turn_scores[i] = b + turns[i+1][0] + turns[i+2][0]
        else: turn_scores[i] = b + turns[i+1][0] + turns[i+1][1]
    elif turns[i][0] + turns[i][1] == b:
        turn_scores[i] = b + turns[i+1][0]
    else:
        turn_scores[i] = turns[i][0] + turns[i][1]

print(sum(turn_scores))
