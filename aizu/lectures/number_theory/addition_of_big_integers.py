# coding: utf-8

# 文字列として処理

A, B = input().split(' ')
rst = ''

minus_A, minus_B = 1, 1
if A[0] == '-':
    minus_A = -1
    A = A[1:]
if B[0] == '-':
    minus_B = -1
    B = B[1:]

max_len = len(A) if len(A) > len(B) else len(B)
carry = 0
for i in range(1, max_len+1):
    ad = int(A[-i]) if i <= len(A) else 0
    bd = int(B[-i]) if i <= len(B) else 0
    tmp = minus_A*ad + minus_B*bd + carry
    print(tmp, rst)
    if i == max_len:
        if tmp < 0:
            tmp += 1
            _rst = ''
            # 補数
            rst = _rst
        rst = str(tmp) + rst
        carry = tmp//10
        rst = rst.lstrip('0')
        if len(rst) == 0: rst = "0"
    else:
        carry = tmp//10
        rst = str(tmp%10) + rst

print(rst)
