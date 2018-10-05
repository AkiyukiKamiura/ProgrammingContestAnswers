#! python3
# common_divisors.py

def gcd(a, b):
    x, y = [a, b] if a > b else [b, a]
    while y:
        x, y = y, x%y
    return x

n = int(input())
nums = sorted(list(map(int, input().split(' '))))
loops = gcd(nums[0], nums[1])
print(1)
for x in range(2, loops+1):
    flg = True
    for num in nums:
        if num%x != 0:
            flg = False
            break
    if flg:
        print(x)
