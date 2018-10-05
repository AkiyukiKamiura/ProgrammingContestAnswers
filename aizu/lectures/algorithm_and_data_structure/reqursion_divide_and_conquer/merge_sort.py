#! python3
# merge_sort.py

count = 0

def merge(A, left, mid, right):
    global count
    L = A[left: mid]
    R = A[mid: right]
    L.append(10e9 + 1)
    R.append(10e9 + 1)
    i, j = 0, 0
    for k in range(left, right):
        count += 1
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = int((left + right)/2)
        merge_sort(A, left, mid)
        merge_sort(A, mid, right)
        merge(A, left, mid, right)

n = int(input())
S = list(map(int, input().split(' ')))

merge_sort(S, 0, n)
print(' '.join(list(map(str, S))))
print(count)
