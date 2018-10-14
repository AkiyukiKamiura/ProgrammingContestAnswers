#! python3
# coding: utf-8

S = input()
cards = {}

for s in S:
    if s not in cards: cards[s] = 0
    cards[s] += 1

if '*' in cards:
    wild_num = cards.pop('*')
    max_val = 0
    max_key = ''
    for key, val in cards.items():
        if max_val < val:
            max_val = val
            max_key = key
    cards[max_key] += wild_num

if len(cards) == 1:
    print('FourCard')
elif len(cards) == 2:
    if cards[list(cards.keys())[0]] == 2:
        print('TwoPair')
    else:
        print('ThreeCard')
elif len(cards) == 3:
    print('OnePair')
else:
    print('NoPair')
