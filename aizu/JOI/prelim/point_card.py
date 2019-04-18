# coding: utf-8

N, M = list(map(int, input().split(' ')))
cards = [int(input().split(' ')[0]) for i in range(M)]
cards = sorted(cards)

cost = 0
for i in range(1, M):
    if cards[i] >= N: break
    cost += N - cards[i]

print(cost)
