#! python3
# coding: utf-8

T = int(input())
deals = [input() for i in range(T)]

can_eat = True
prior_n = -10
cnt = 0
for i, deal in enumerate(deals):
    if i > prior_n + 10: can_eat = True
    if can_eat and deal == 'melon':
        can_eat = False
        prior_n = i
        cnt += 1

print(cnt)
