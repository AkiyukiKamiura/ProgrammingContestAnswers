#! python3
# min_max_and_sum.py

n = int(input())
a = [int(x) for x in input().split(' ')]

min_val = a[0]
max_val = a[0]
sum_val = a[0]

for i in range(1, n):
    if a[i] < min_val:
        min_val = a[i]
    if a[i] > max_val:
        max_val = a[i]
    sum_val += a[i]

print(min_val, max_val, sum_val)
