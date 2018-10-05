#! python3
# reversing_numbers.py

n = int(input())
a = [int(x) for x in input().split(' ')]

for i in range(1, n+1):
    if i < n:
        print(str(a[-1*i]) + ' ', end='')
    else:
        print(str(a[-1*i]))
