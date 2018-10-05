#! python3
# how_many_ways.py

while True:
    n, x = [int(i) for i in input().split(' ')]
    if n == 0 and x == 0: break

    combis = 0
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if x - i - j > j and x - i - j <= n:
                combis += 1
    print(combis)
