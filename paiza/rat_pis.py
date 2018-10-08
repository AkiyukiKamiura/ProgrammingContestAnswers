#! python3
# coding: utf-8

def print_field(field):
    for row in field[1:-1]:
        print(''.join(row[1:-1]))

class Directions:
    def __init__(self, first):
        self.directions = {'north': [0, -1], 'south': [0, 1], 'west': [-1, 0], 'east': [1, 0]}
        self.now = first

    def turn_right(self):
        if self.now == 'north': self.now = 'east'
        elif self.now == 'east': self.now = 'south'
        elif self.now == 'south': self.now = 'west'
        elif self.now == 'west': self.now = 'north'

    def turn_left(self):
        if self.now == 'north': self.now = 'west'
        elif self.now == 'west': self.now = 'south'
        elif self.now == 'south': self.now = 'east'
        elif self.now == 'east': self.now = 'north'

    def move_dir(self):
        return self.directions[self.now]

H, W = list(map(int, input().split(' ')))
h0, w0 = list(map(int, input().split(' ')))

field = [['o' for w in range(W+2)] for h in range(H+2)]
for h in range(1, H+1):
    field[h][1:W+1] = list(input())

now_h, now_w = h0, w0
rat_dir = Directions('north')
while field[now_h][now_w] != 'o':
    if field[now_h][now_w] == '*':
        field[now_h][now_w] = '.'
        rat_dir.turn_left()
    elif field[now_h][now_w] == '.':
        field[now_h][now_w] = '*'
        rat_dir.turn_right()

    dir = rat_dir.move_dir()
    now_h += dir[1]
    now_w += dir[0]

print_field(field)
