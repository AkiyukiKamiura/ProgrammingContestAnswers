#! python3
# map_search.py

dict = {}
q = int(input())
for i in range(q):
    query, *val = input().split(' ')
    if query == '0':
        dict[val[0]] = int(val[1])
    elif query == '1':
        print(dict.get(val[0], 0))
