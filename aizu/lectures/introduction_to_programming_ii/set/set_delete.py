#! python3
# set_delete.py

numset = set([])
q = int(input())
for i in range(q):
    query = list(map(int, input().split(' ')))
    x = query[1]
    if query[0] == 0:
        numset.add(x)
        print(len(numset))
    elif query[0] == 1:
        if set([x]).issubset(numset):
            print(1)
        else:
            print(0)
    elif query[0] == 2:
        if set([x]).issubset(numset):
            numset.remove(x)
    else:
        L, R = query[1:]
