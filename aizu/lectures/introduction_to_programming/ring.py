#! python3
# ring.py

sent = input()
pat = input()

len_sent = len(sent)
len_pat = len(pat)

flag = False
for i in range(len_sent):
    sent_pat = ''
    if i+len_pat <= len_sent:
        sent_pat = sent[i:i+len_pat]
    else:
        sent_pat = sent[i:len_sent] + sent[0:len_pat - (len_sent - i)]
    if sent_pat == pat:
        flag = True

if flag:
    print('Yes')
else:
    print('No')
