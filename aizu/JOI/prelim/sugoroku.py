# coding: utf-8

N = int(input())
A = list(map(int, input().split(' ')))
max_sequence = 0
seq = 0

for a in A:
    seq = seq + 1 if a == 1 else 0
    if max_sequence < seq: max_sequence = seq

print(max_sequence + 1)
