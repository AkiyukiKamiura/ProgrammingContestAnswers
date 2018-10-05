#! python3
# count.py

n = int(input())
nums = list(map(int, input().split(' ')))

q = int(input())
for i in range(q):
    op =  list(map(int, input().split(' ')))
    print(nums[op[0]:op[1]].count(op[2]))
