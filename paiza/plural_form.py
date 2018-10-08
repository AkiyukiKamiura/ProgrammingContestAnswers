#! python3
# coding: utf-8

# TODO: やり直し

import re

es_pat = re.compile(r".+[s|sh|ch|o|x]")
ves_pat = re.compile(r".+(fe|f)")
ies_pat = re.compile(r".+[^aiueo]y")

N = int(input())
for n in range(N):
    word = input()
    es_ob = re.match(es_pat, word)
    ves_ob = re.match(ves_pat, word)
    ies_ob = re.match(ies_pat, word)

    if es_ob != None and es_ob.end() == len(word):
        word += 'es'
    elif ves_ob != None and ves_ob.end() == len(word):
        word = word[:len(word) - len(ves_ob.group(1))] + 'ves'
    elif ies_ob != None and ies_ob.end() == len(word):
        word = word[:len(word)-1] + 'ies'
    else:
        word += 's'

    print(word)
