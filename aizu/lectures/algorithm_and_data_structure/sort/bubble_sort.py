#! python3
# bubble_sort.py

# 泡が上がっていくようにソーティングされる

N = int(input())
A = [int(x) for x in input().split(' ')]

exc_num = 0
flag = True
while flag:
    flag = False
    for i in range(N-1, 0, -1):
        if A[i] < A[i-1]:
            exc_num += 1
            A[i-1], A[i] = A[i], A[i-1]
            flag = True

print(' '.join([str(x) for x in A]))
print(exc_num)
