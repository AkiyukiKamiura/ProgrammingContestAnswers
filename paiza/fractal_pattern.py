#! python3
# coding: utf-8

K = int(input())
N = int(input())
basic_pattern = [list(input()) for i in range(N)]
prior_pattern = basic_pattern
prior_N = N
for _ in range(K):
    new_N = pow(prior_N, 2)
    new_pattern = [['' for c in range(new_N)] for r in range(new_N)]
    for r in range(prior_N):
        for c in range(prior_N):
            if prior_pattern[r][c] == '#':
                top = r * prior_N
                left = c * prior_N
                for _r in range(prior_N):
                    for _c in range(prior_N):
                        new_pattern[top + _r][left + _c] = prior_pattern[_r][_c]
            elif prior_pattern[r][c] == '.':
                top = r * prior_N
                left = c * prior_N
                for _r in range(prior_N):
                    for _c in range(prior_N):
                        new_pattern[top + _r][left + _c] = '.'
    prior_N = new_N
    prior_pattern = new_pattern

for row in prior_pattern:
    print(''.join(row))
