#! python3
# counting_characters.py

import sys

sents = [line.strip() for line in sys.stdin.readlines()]
dic = {chr(x):0 for x in range(ord('a'), ord('z')+1)}

for sent in sents:
    for c in sent:
        x = c.lower()
        if ord('a') <= ord(x) and ord(x) <= ord('z'):
            dic[x] += 1

for k, v in dic.items():
    print(k + ' : ' + str(v))
