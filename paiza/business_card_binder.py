#! python3
# coding: utf-8

import math

n, m = list(map(int, input().split(' ')))

file_num = math.floor((m-1)/(n*2))
prior_file_last = file_num*n*2
print(prior_file_last + (n*2+1-(m-prior_file_last)))
