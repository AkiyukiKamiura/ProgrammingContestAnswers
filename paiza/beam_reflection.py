#! python3
# coding: utf-8

H, W = list(map(int, input().split(' ')))
field = [['e' for w in range(W+2)] for h in range(H+2)]
for h in range(1, H+1):
    field[h][1:W+1] = list(repr(input()).replace('\\\\', '\\')[1:-1])
directions = {'right': [1, 0], 'left': [-1, 0], 'up': [0, -1], 'down': [0, 1]}

x, y, dir = 1, 1, 'right'
def reflection(x, y, dir):
    global field, directions
    next_x, next_y, next_dir = x, y, dir
    if field[y][x] == '\\':
        if dir == 'right': next_dir = 'down'
        elif dir == 'down': next_dir = 'right'
        elif dir == 'left': next_dir = 'up'
        elif dir == 'up': next_dir = 'left'
    elif field[y][x] == '/':
        if dir == 'right': next_dir = 'up'
        elif dir == 'up': next_dir = 'right'
        elif dir == 'left': next_dir = 'down'
        elif dir == 'down': next_dir = 'left'
    move_dir = directions[next_dir]
    next_x += move_dir[0]
    next_y += move_dir[1]
    return next_x, next_y, next_dir

count = 0
while field[y][x] != 'e':
    count += 1
    x, y, dir = reflection(x, y, dir)

print(count)
