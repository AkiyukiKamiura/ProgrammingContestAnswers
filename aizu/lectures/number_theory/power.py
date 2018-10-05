#! python3
# power.py

MAX = 1000000007

m, n = [int(x) for x in input().split(' ')]
bi_n = bin(n)

ans = 1
dig = m
for i in range(len(bi_n)-1, 1, -1):
    if bi_n[i] == '1': ans *= dig
    if ans >= MAX: ans %= MAX
    dig *= dig
    if dig >= MAX: dig %= MAX

print(ans)
