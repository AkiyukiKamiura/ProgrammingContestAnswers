#! python3
# prime_number.py

import math

def is_prime_number(x):
    if x < 2: return False
    elif x == 2: return True
    elif x%2 == 0: return False

    sqrt_upper_bound = math.floor(math.sqrt(x))+1
    for i in range(3, sqrt_upper_bound, 2):
        if x % i == 0:
            return False

    return True

n = int(input())
prime_num = 0
for i in range(n):
    x = int(input())
    if is_prime_number(x):
        prime_num += 1

print(prime_num)
