#! python3
# transformation.py

sent = input()

def print_(arr):
    global sent
    print(sent[int(arr[0]):int(arr[1])+1])

def reverse_(arr):
    global sent
    sent = sent[:int(arr[0])] + sent[int(arr[0]):int(arr[1])+1][::-1] + sent[int(arr[1])+1:]

def replace_(arr):
    global sent
    sent = sent[:int(arr[0])] + arr[2] + sent[int(arr[1])+1:]

ops = {'print': print_, 'reverse': reverse_, 'replace': replace_}

q = int(input())
for i in range(q):
    arr = input().split()
    ops[arr[0]](arr[1:])
