#! python3
# selection_sort.py

# 各ステップで最小値を選択

n = int(input())
A = [int(x) for x in input().split(' ')]

exc_num = 0
for i in range(n-1):
    minj = i
    for j in range(i, n):
        if A[j] < A[minj]:
            minj = j
    if i != minj:
        exc_num += 1
        A[i], A[minj] = A[minj], A[i]

print(' '.join([str(x) for x in A]))
print(exc_num)
