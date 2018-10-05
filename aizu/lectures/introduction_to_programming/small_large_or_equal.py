#! python3
# small_large_or_equal.py

a, b = [int(x) for x in input().split(' ')]
if a < b:
    print('a < b')
elif a == b:
    print('a == b')
else:
    print('a > b')
