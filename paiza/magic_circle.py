#! python3

N = int(input())
magic_circle = []
for i in range(N):
    magic_circle.append(list(map(int, input().split(' '))))

covered_index = []
for c in range(N):
    for r in range(N):
        if magic_circle[r][c] == 0:
            covered_index.append(c)
            covered_index.append(r)

target_sum = (N*N + 1)/2 * N
c1, r1, c2, r2 = covered_index

if c1 == c2:
    # 列が同じ
    magic_circle[r1][c1] = int(target_sum - sum(magic_circle[r1]))
    magic_circle[r2][c2] = int(target_sum - sum(magic_circle[r2]))
else:
    magic_circle[r1][c1] = int(target_sum - sum([row[c1] for row in magic_circle]))
    magic_circle[r2][c2] = int(target_sum - sum([row[c2] for row in magic_circle]))

for row in magic_circle:
    print(' '.join(list(map(str, row))))
