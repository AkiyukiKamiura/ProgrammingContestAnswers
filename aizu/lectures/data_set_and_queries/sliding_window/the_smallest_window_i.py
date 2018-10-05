#! python3
# the_smallest_window_i.py

n, s = list(map(int, input().split()))
a = list(map(int, input().split()))

ans = None
init_sum = 0
for window in range(n):
    init_sum += a[window]
    sum_a = init_sum
    for i in range(n-window):
        if i != 0:
            sum_a += a[i+window] - a[i-1]
        if sum_a >= s:
            ans = window+1
            break
    if ans != None: break

if ans == None: ans = 0
print(ans)
