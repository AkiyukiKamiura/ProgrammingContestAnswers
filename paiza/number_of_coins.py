#! python3
# coding: utf-8

import copy

def get_just_coins(x):
    coins = { 500: 0, 100: 0, 50: 0, 10: 0, 5: 0, 1: 0 }
    for k in coins.keys():
        coins[k] = x//k
        x -= k * (x//k)
    return coins

def increment_coins(coins):
    vals = sorted(coins.keys())
    flg = False
    for i, v in enumerate(vals):
        if flg:
            coins[v] += 1
            break
        if coins[v] != 0:
            coins[v] = 0
            flg = True

def exchange_coins(coins):
    vals = sorted(coins.keys())
    for i, v in enumerate(vals[:-1]):
        if coins[v] * v >= vals[i+1]:
            coins[v] -= vals[i+1]//v
            coins[vals[i+1]] += 1

x = int(input())
coins = get_just_coins(x)

min_coins = 1000
while sum(coins.values()) != 0:
    cnum = sum(coins.values())
    value = sum([k*v for k, v in coins.items()])

    ret_coins = get_just_coins(value - x)
    ret_cnum = sum(ret_coins.values())
    if cnum + ret_cnum < min_coins:
        min_coins = cnum + ret_cnum

    increment_coins(coins)
    exchange_coins(coins)

print(min_coins)
