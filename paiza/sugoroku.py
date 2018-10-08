#! python3
# coding: utf-8

import numpy as np

class Dice:
    def __init__(self, T, B, U, D, L, R):
        self.surfaces = {'top': T, 'bottom': B, 'up': U, 'down': D, 'left': L, 'right': R}
        self.top_dir = np.array([0, 0, 1]) # top が向いている方向
        self.up_dir = np.array([1, 0, 0]) # up が向いている方向
        self.right_dir = np.array([0, 1, 0]) # right が向いている方向

    def top_pos_num(self, top_dir, up_dir, right_dir):
        if (top_dir == [0, 0, 1]).all(): return self.surfaces['top']
        elif (top_dir == [0, 0, -1]).all(): return self.surfaces['bottom']
        elif (up_dir == [0, 0, 1]).all(): return self.surfaces['up']
        elif (up_dir == [0, 0, -1]).all(): return self.surfaces['down']
        elif (right_dir == [0, 0, 1]).all(): return self.surfaces['right']
        elif (right_dir == [0, 0, -1]).all(): return self.surfaces['left']

    def bottom_pos_num(self, top_dir, up_dir, right_dir):
        if (top_dir == [0, 0, 1]).all(): return self.surfaces['bottom']
        elif (top_dir == [0, 0, -1]).all(): return self.surfaces['top']
        elif (up_dir == [0, 0, 1]).all(): return self.surfaces['down']
        elif (up_dir == [0, 0, -1]).all(): return self.surfaces['up']
        elif (right_dir == [0, 0, 1]).all(): return self.surfaces['left']
        elif (right_dir == [0, 0, -1]).all(): return self.surfaces['right']

    def rotate_x(self, deg):
        r = np.radians(deg)
        co = np.cos(r)
        si = np.sin(r)
        R_x = np.matrix([[1, 0, 0], [0, co, -si], [0, si, co]])
        return R_x

    def rotate_y(self, deg):
        r = np.radians(deg)
        co = np.cos(r)
        si = np.sin(r)
        R_y = np.matrix([[co, 0, -si], [0, 1, 0], [si, 0, co]])
        return R_y

    def dot_mat(self, mat, dir):
        rst = mat.dot(dir)
        rst = np.array(rst, dtype=np.int8)
        return rst[0]

    def rotate(self, target, next_target):
        if self.top_pos_num(self.top_dir, self.up_dir, self.right_dir) == target: return 0

        rotation_list = [self.rotate_y(90), self.rotate_y(-90), self.rotate_x(90), self.rotate_x(-90)] # ok
        for rot in rotation_list:
            new_top_dir = self.dot_mat(self.top_dir, rot)
            new_up_dir = self.dot_mat(self.up_dir, rot)
            new_right_dir = self.dot_mat(self.right_dir, rot)
            if target == self.top_pos_num(new_top_dir, new_up_dir, new_right_dir):
                self.top_dir = new_top_dir
                self.up_dir = new_up_dir
                self.right_dir = new_right_dir
                return 1

        twice_rotation_list = [self.rotate_y(180), self.rotate_x(180)]
        for i, rot in enumerate(twice_rotation_list):
            new_top_dir = self.dot_mat(self.top_dir, rot)
            new_up_dir = self.dot_mat(self.up_dir, rot)
            new_right_dir = self.dot_mat(self.right_dir, rot)
            if next_target != self.bottom_pos_num(new_top_dir, new_up_dir, new_right_dir) or i == 1:
                self.top_dir = new_top_dir
                self.up_dir = new_up_dir
                self.right_dir = new_right_dir
                return 2

T, B, U, D, L, R = list(map(int, input().split(' ')))
dice = Dice(T, B, U, D, L, R)
N = int(input())
field = [int(input()) for n in range(N)]
field.append(None)
rotate_num = 0
for n in range(1, N):
    rotate_num += dice.rotate(field[n], field[n+1])

print(rotate_num)
