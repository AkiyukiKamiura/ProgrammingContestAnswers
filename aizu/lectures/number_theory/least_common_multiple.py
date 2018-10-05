#! python3
# least_commom_multiple.py

# ユークリッドの互除法
def gcd(a, b):
    x, y = [a, b] if a > b else [b, a]
    while y:
        x, y = y, x%y
    return x

def lcm(a, b):
    return a*b // gcd(a, b)

n = int(input())
A = [int(x) for x in input().split(' ')]

tmp = A[0]
for i in range(1, n):
    tmp = lcm(tmp, A[i])

print(tmp)
