#! python3
# coding: utf-8

import numpy as np

d_to_a = {'0': '*|=|****', '1': '*|=*|***', '2': '*|=**|**', '3': '*|=***|*', '4': '*|=****|',
          '5': '|*=|****', '6': '|*=*|***', '7': '|*=**|**', '8': '|*=***|*', '9': '|*=****|'}
a_to_d = {'*|=|****': '0', '*|=*|***': '1', '*|=**|**': '2', '*|=***|*': '3', '*|=****|': '4',
          '|*=|****': '5', '|*=*|***': '6', '|*=**|**': '7', '|*=***|*': '8', '|*=****|': '9'}

n = int(input())
abacus_1 = np.array([list(input()) for i in range(8)]).T
abacus_2 = np.array([list(input()) for i in range(8)]).T
abacus_1 = [''.join(abacus_1[i]) for i in range(n)]
abacus_2 = [''.join(abacus_2[i]) for i in range(n)]

num1, num2 = '', ''
for a in abacus_1:
    num1 += a_to_d[a]
for a in abacus_2:
    num2 += a_to_d[a]

ans_dig = str(int(num1) + int(num2))
ans_aba = [list(d_to_a[d]) for d in ans_dig]
ans_aba = [list(d_to_a['0'])]*(n-len(ans_dig)) + ans_aba
ans_aba = np.array(ans_aba).T

for row in ans_aba:
    print(''.join(row))
