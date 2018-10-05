#! python3
# swapping_two_numbers.py

for i in range(3000):
    x, y = [int(n) for n in input().split(' ')]
    if x == 0 and y == 0:
        break

    if x < y:
        print(x, y)
    else:
        print(y, x)
