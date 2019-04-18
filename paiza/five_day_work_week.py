#! python3
# coding: utf-8

N = int(input())
schedule = list(map(int, input().split(' ')))

cv = schedule[:7].count(0)
max_cont = 0 if cv < 2 else 7
num_cont = max_cont

for i in range(7, N):
    new_day = schedule[i]
    last_day = schedule[i-7]
    if new_day == 0: cv += 1
    if last_day == 0: cv -= 1

    if cv >= 2:
        if num_cont == 0:
            num_cont = 7
        else:
            num_cont += 1
    else:
        num_cont = 0

    if num_cont > max_cont: max_cont = num_cont

print(max_cont)
