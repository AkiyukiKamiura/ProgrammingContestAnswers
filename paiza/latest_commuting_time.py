#! python3

import math

class Time:
    def __init__(self, h, m):
        self.h = h
        self.m = m

    def get_minutes(self):
        return self.h * 60 + self.m

    def add_minute(self, m):
        self.m += m
        if self.m >= 60 or self.m < 0:
            self.h += math.floor(self.m / 60)
            self.m = self.m%60

    def print_time(self):
        str_h, str_m = str(self.h), str(self.m)
        if len(str_h) == 1: str_h = '0' + str_h
        if len(str_m) == 1: str_m = '0' + str_m
        print(str_h + ':' + str_m)

latest_arrival = Time(8, 59)

a, b, c = list(map(int, input().split(' ')))
N = int(input())

usable_train = Time(0, 0)
time_table = [list(map(int, input().split(' '))) for i in range(N)]
for i in range(N):
    h, m = time_table[i]

    arrival = Time(h, m)
    arrival.add_minute(b + c)

    if latest_arrival.get_minutes() >= arrival.get_minutes():
        usable_train.h = h
        usable_train.m = m
    else:
        break

starting = Time(usable_train.h, usable_train.m)
starting.add_minute(-a)
starting.print_time()
