#! python3
# coding: utf-8

import numpy as np

class Robot:
    def __init__(self, x, y, dir, d_f, d_r, d_b, d_l):
        self.pos = np.array([x, y])
        self.dir = dir
        self.move_to = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]
        self.move_amount = [d_f, d_r, d_b, d_l]

    def move(self, dir):
        if dir == 'F':
            self.pos += self.move_to[self.dir] * self.move_amount[0]
        elif dir == 'R':
            if self.dir <= 2:
                self.pos += self.move_to[self.dir+1] * self.move_amount[1]
            else:
                self.pos += self.move_to[self.dir-3] * self.move_amount[1]
        elif dir == 'L':
            if 1 <= self.dir:
                self.pos += self.move_to[self.dir-1] * self.move_amount[3]
            else:
                self.pos += self.move_to[self.dir+3] * self.move_amount[3]
        elif dir == 'B':
            if 2 <= self.dir:
                self.pos += self.move_to[self.dir-2] * self.move_amount[2]
            else:
                self.pos += self.move_to[self.dir+2] * self.move_amount[2]

    def turn(self, dir):
        if dir == 'R':
            if self.dir <= 2:
                self.dir = self.dir+1
            else:
                self.dir = self.dir-3
        elif dir == 'L':
            if 1 <= self.dir:
                self.dir = self.dir-1
            else:
                self.dir = self.dir+3
        elif dir == 'B':
            if 2 <= self.dir:
                self.dir = self.dir-2
            else:
                self.dir = self.dir+2

s_x, s_y = list(map(int, input().split(' ')))
d_f, d_r, d_b, d_l = list(map(int, input().split(' ')))
robot = Robot(s_x, s_y, 0, d_f, d_r, d_b, d_l)

N = int(input())
for _ in range(N):
    ope, dir = input().split(' ')
    if ope == 'm':
        robot.move(dir)
    elif ope == 't':
        robot.turn(dir)

print(' '.join(list(map(str, list(robot.pos)))))
