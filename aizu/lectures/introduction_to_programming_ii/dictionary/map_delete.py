#! python3
# map_search.py

from collections import OrderedDict

dict = OrderedDict()

q = int(input())
for i in range(q):
    query, *val = input().split(' ')
    if query == '0':
        dict[val[0]] = int(val[1])
    elif query == '1':
        print(dict.get(val[0], 0))
    elif query == '2':
        if val[0] in dict:
            dict.pop(val[0])
    else:
        ans = ''
        for k, v in dict.items():
            if val[0] <= k and k <= val[1]:
                ans += str(k) + ' ' + str(v) + ' '
        print(ans.strip())
