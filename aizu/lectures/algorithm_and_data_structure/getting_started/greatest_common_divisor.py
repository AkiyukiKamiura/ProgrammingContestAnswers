#! python3
# greatest_common_divisor.py

def gcd(a, b):
    x, y = [a, b] if a > b else [b, a]
    while y:
        x, y = y, x%y
    return x

x, y = [int(n) for n in input().split(' ')]
print(gcd(x, y))
