#! python3
# coding: utf-8

# シーザー暗号

n, T = input().split(' ')
n = int(n)
S = input()

alphabets = 'abcdefghijklmnopqrstuvwxyz'
decryption = {}
for i in range(26):
    decryption[T[i]] = alphabets[i]

ans = S
for i in range(n):
    new_ans = ''
    for s in ans:
        if s == ' ': new_ans += ' '
        else: new_ans += decryption[s]
    ans = new_ans
print(ans)
