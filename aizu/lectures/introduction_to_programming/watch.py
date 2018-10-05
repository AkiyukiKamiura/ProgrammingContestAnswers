#! python3
# watch.py

import math

S = int(input())
h = math.floor(S/3600)
m = math.floor((S%3600)/60)
s = math.floor((S%60))
print(str(h) + ':' + str(m) + ':' + str(s))
