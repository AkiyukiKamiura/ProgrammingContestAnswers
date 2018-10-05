#! python3
# finding_a_word.py

W = input()
sents = []
while True:
    sent = input()
    if sent == 'END_OF_TEXT' :break
    sents.append(sent.lower())

word_ct = 0
for sent in sents:
    for word in sent.split(' '):
        word = word.strip('\.\,\:\"\'')
        if word == W:
            word_ct += 1

print(word_ct)
