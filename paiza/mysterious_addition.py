#! python3
# coding: utf-8

import math

paiza_num = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4}
num_paiza = ['A', 'B', 'C', 'D', 'E']

def paiza_to_decimal(pai):
    global paiza_num
    dec = 0
    for i, val in enumerate(list(pai)[::-1]):
        dec += paiza_num[val]*pow(5, i)
    return dec

def decimal_to_paiza(dec):
    global num_paiza
    pai = ''
    while 5 <= dec:
        rem = dec - math.floor(dec/5)*5
        pai = num_paiza[rem] + pai
        dec = math.floor(dec/5)
    pai = num_paiza[dec] + pai
    return pai

S1, S2 = input().split(' ')
print(decimal_to_paiza(paiza_to_decimal(S1) + paiza_to_decimal(S2)))
