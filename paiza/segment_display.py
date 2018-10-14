#! python3
# coding: utf-8

numbers = ['1111110', '0110000', '1101101', '1111001', '0110011', '1011011', '1011111', '1110010', '1111111', '1111011']

def print_dis(a, b):
    indexes_a = [[0, 1], [1, 2], [3, 2], [4, 1], [3, 0], [1, 0], [2, 1]]
    indexes_b = [[0, 4], [1, 5], [3, 5], [4, 4], [3, 3], [1, 3], [2, 4]]

    disp = [[' ' for i in range(6)] for j in range(5)]
    for i in range(len(a)):
        pos = indexes_a[i]
        if a[i] == '1':
            if pos[0]%2 == 1:
                disp[pos[0]][pos[1]] = '|'
            else:
                disp[pos[0]][pos[1]] = '-'
        pos = indexes_b[i]
        if b[i] == '1':
            if pos[0]%2 == 1:
                disp[pos[0]][pos[1]] = '|'
            else:
                disp[pos[0]][pos[1]] = '-'

    for row in disp:
        print(''.join(row))

a = input().split(' ')
b = input().split(' ')

print_dis(a, b)

current_pos = 'No'
mirrored_pos = 'No'
rotated_pos = 'No'

if ''.join(a) in numbers and ''.join(b): current_pos = 'Yes'
mirrored_a, mirrored_b = [b[0], b[5], b[4], b[3], b[2], b[1], b[6]], [a[0], a[5], a[4], a[3], a[2], a[1], a[6]]
print_dis(mirrored_a, mirrored_b)
if ''.join(mirrored_a) in numbers and ''.join(mirrored_b): mirrored_pos = 'Yes'
rotated_a, rotated_b = [b[3], b[4], b[5], b[0], b[1], b[2], b[6]], [a[3], a[4], a[5], a[0], a[1], a[2], a[6]]
print_dis(rotated_a, rotated_b)
if ''.join(rotated_a) in numbers and ''.join(rotated_b): rotated_pos = 'Yes'

print(current_pos)
print(mirrored_pos)
print(rotated_pos)
