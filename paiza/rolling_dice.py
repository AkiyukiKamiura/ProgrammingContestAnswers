# coding: utf-8

class Dice():
    def __init__(self):
        self.top = 1
        self.right = 4
        self.left = 3
        self.bottom = 6
        self.front = 5
        self.back = 2

    def roll_right(self):
        self.top, self.right, self.bottom, self.left = self.left, self.top, self.right, self.bottom

    def roll_left(self):
        self.top, self.right, self.bottom, self.left = self.right, self.bottom, self.left, self.top

    def roll_back(self):
        self.top, self.back, self.bottom, self.front = self.front, self.top, self.back, self.bottom

    def roll_front(self):
        self.top, self.back, self.bottom, self.front = self.back, self.bottom, self.front, self.top

N, H, W = list(map(int, input().split(' ')))
sy, sx = list(map(int, input().split(' ')))
operation = input()

flag_canvas = [[0 for i in range(W)] for j in range(H)]
dice = Dice()
y, x = sy-1, sx-1
flag_canvas[y][x] = dice.bottom

for ope in operation:
    if ope == 'U':
        dice.roll_back()
        y -= 1
    elif ope == 'D':
        dice.roll_front()
        y += 1
    elif ope == 'R':
        dice.roll_right()
        x += 1
    elif ope == 'L':
        dice.roll_left()
        x -= 1
    flag_canvas[y][x] = dice.bottom

for row in flag_canvas:
    print(' '.join(list(map(str, row))))
