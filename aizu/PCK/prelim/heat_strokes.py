# coding: utf-8

import math

A, B, X = list(map(int, input().split(' ')))

cost = math.floor(X/1000)*A if A <= 2*B else math.floor(X/1000)*B*2
