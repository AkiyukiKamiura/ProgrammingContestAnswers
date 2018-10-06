#! python3

M, N, K = list(map(int, input().split(' ')))

electorates = [0 for x in range(M+1)]
electorates[0] = N

for k in range(K):
    ele_m = int(input())
    for m in range(M+1):
        if ele_m == m: continue
        if electorates[m] >= 1:
            electorates[ele_m] += 1
            electorates[m] -= 1

max_num = max(electorates[1:])
for m in range(1, M+1):
    if max_num == electorates[m]:
        print(m)
