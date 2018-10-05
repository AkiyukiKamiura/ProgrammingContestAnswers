#! python3
# maximum_heap.py

n = int(input())
H = list(map(int, input().split(' ')))

def max_heapify(i):
    l = (i+1)*2-1
    r = (i+1)*2
    largest = i
    if l < n and H[l] > H[i]:
        largest = l
    else:
        largest = i
    if r < n and H[r] > H[largest]:
        largest = r

    if largest != i:
        H[i], H[largest] = H[largest], H[i]
        max_heapify(largest)

def print_elements(lst):
    for ele in lst:
        print(' {}'.format(ele), end='')
    print('')

for i in range(int(n/2), -1, -1):
    max_heapify(i)

print_elements(H)
