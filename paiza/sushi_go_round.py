#! python3
# coding: utf-8

import numpy as np

class Customer:
    def __init__(self, pos):
        self.pos = pos
        self.eating = False
        self.time = 0
        self.eating_start_time = 0

    def increment_time(self):
        self.time += 1
        if self.eating == True and self.time - self.eating_start_time == 10:
            self.eating = False
            self.eating_start_time = -1

    def eat(self):
        if self.eating == True: return 0
        self.eating = True
        self.eating_start_time = self.time

    def can_eat(self):
        return not self.eating

class Lane:
    def __init__(self, round_time):
        self.round_time = round_time
        self.sushi = np.array([False for i in range(round_time)])
        self.sushi_num = 0
        self.time = 0

    def set_sushi(self, pos):
        self.sushi[pos] = True
        self.sushi_num += 1

    def increment_time(self, adding_sushi=None):
        self.sushi = np.roll(self.sushi, 1)
        self.time += 1

    def available_sushi(self, pos):
        return self.sushi[pos]

    def taken(self, pos):
        self.sushi[pos] = False
        self.sushi_num -= 1

L, N, M = list(map(int, input().split(' ')))
lane = Lane(L)
customers = [Customer(int(x)) for x in input().split(' ')]
for s in input().split(' '): lane.set_sushi(int(s))

while True:
    for cus in customers:
        if lane.available_sushi(cus.pos) and cus.can_eat():
            cus.eat()
            lane.taken(cus.pos)

    if lane.sushi_num == 0:
        waiting_num = 0
        for cus in customers:
            if cus.can_eat(): waiting_num += 1
        if waiting_num == N: break

    lane.increment_time()
    for cus in customers: cus.increment_time()

print(lane.time)
