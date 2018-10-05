#! python3
# sorting_three_numbers.py

nums = [int(x) for x in input().split()]

sorted_nums = []
sorted_nums.append(nums[0])

if nums[1] <= sorted_nums[0]:
    sorted_nums.insert(0, nums[1])
else:
    sorted_nums.append(nums[1])

if nums[2] <= sorted_nums[0]:
    sorted_nums.insert(0, nums[2])
elif nums[2] > sorted_nums[-1]:
    sorted_nums.append(nums[2])
else:
    sorted_nums.insert(1, nums[2])

print(' '.join([str(x) for x in sorted_nums]))
