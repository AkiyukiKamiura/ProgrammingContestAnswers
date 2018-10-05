#! python3
# official_house.py

n = int(input())
rooms = [[int(x) for x in input().split(' ')] for i in range(n)]

rooms_people = [[[0 for k in range(10)] for j in range(3)] for i in range(4)]
for i in range(n):
    rooms_people[rooms[i][0]-1][rooms[i][1]-1][rooms[i][2]-1] += rooms[i][3]

for i in range(4):
    if i != 0: print('####################')
    for j in range(3):
        for k in range(10):
            print('', rooms_people[i][j][k], end='')
        print('')
