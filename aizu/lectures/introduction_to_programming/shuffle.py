#! python3
# shuffle.py

def shuffle(text, n):
    return text[n:] + text[:n]

while True:
    sent = input()
    if sent == '-': break
    m = int(input())

    h = 0
    for i in range(m):
        h += int(input())
    h = h % len(sent)

    sent = shuffle(sent, h)
    print(sent)
