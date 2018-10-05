#! python3
# maximum_profit.py

n = int(input())
R = [int(input()) for i in range(n)]

min_i = 0
max_val = R[1]-R[0]
max_j = -1
for i in range(n-1):
    if R[min_i] < R[i]:
        continue
    elif R[min_i] > R[i]:
        min_i = i

    if max_j <= i:
        max_j = i+1
        for j in range(i+1, n):
            if R[max_j] < R[j]:
                max_j = j

    if max_val < R[max_j] - R[min_i]:
        max_val = R[max_j] - R[min_i]

print(max_val)
