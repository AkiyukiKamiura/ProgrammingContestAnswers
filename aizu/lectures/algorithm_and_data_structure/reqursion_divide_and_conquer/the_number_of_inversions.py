#! python3
# the_number_of_inversions.py

def merge(A, left, mid, right):
    count = 0
    L = A[left: mid]
    R = A[mid: right]
    L.append(10e9 + 1)
    R.append(10e9 + 1)
    i, j = 0, 0
    for k in range(left, right):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            count += (len(L)-1) - i
    return count

def merge_sort(A, left, right):
    if left + 1 < right:
        mid = int((left + right)/2)
        v1 = merge_sort(A, left, mid)
        v2 = merge_sort(A, mid, right)
        v3 = merge(A, left, mid, right)
        return v1 + v2 + v3
    else:
        return 0

n = int(input())
A = list(map(int, input().split(' ')))

ans = merge_sort(A, 0, n)
print(ans)
