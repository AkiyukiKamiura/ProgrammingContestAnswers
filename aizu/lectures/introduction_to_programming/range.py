#! python3
# range.py

a, b, c = [int(x) for x in input().split()]
if a < b and b < c:
    print('Yes')
else:
    print('No')
