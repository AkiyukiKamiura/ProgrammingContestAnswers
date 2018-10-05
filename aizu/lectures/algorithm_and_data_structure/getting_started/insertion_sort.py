#! python3
# insertion_sort.py

N = int(input())
nums = [int(x) for x in input().split(' ')]

print(' '.join([str(x) for x in nums]))
for i in range(1, N):
    v = nums[i]
    j = i-1
    while j >= 0 and nums[j] > v:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = v
    print(' '.join([str(x) for x in nums]))
