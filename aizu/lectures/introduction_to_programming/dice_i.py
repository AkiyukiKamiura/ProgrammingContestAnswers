#! python3
# dice_i.py

class dice():
    def __init__(self, arr):
        self.top = arr[0]
        self.south = arr[1]
        self.east = arr[2]
        self.west = arr[3]
        self.north = arr[4]
        self.bottom = arr[5]

    def rotate(self, ope):
        if ope == 'S':
            self.top, self.north, self.bottom, self.south = self.north, self.bottom, self.south, self.top
        elif ope == 'N':
            self.top, self.south, self.bottom, self.north = self.south, self.bottom, self.north, self.top
        elif ope == 'E':
            self.top, self.west, self.bottom, self.east = self.west, self.bottom, self.east, self.top
        elif ope == 'W':
            self.top, self.east, self.bottom, self.west = self.east, self.bottom, self.west, self.top

dc = dice([int(x) for x in input().split(' ')])
opes = list(input())

for op in opes:
    dc.rotate(op)

print(dc.top)
