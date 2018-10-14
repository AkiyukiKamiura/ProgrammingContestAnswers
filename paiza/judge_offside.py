#! python3
# coding: utf-8

T, U = input().split()
U = int(U)
team_A = list(map(int, input().split(' ')))
team_B = list(map(int, input().split(' ')))

offside_member = []
if T == 'A':
    enemy_line = sorted(team_B)[-2]
    for i, mem in enumerate(team_A):
        if 55 <= mem and team_A[U-1] < mem and enemy_line < mem:
            offside_member.append(i+1)
elif T == 'B':
    enemy_line = sorted(team_A)[1]
    for i, mem in enumerate(team_B):
        if mem <= 55 and mem < team_B[U-1] and mem < enemy_line:
            offside_member.append(i+1)

if len(offside_member) == 0: print('None')
else:
    for mem in offside_member:
        print(mem)
