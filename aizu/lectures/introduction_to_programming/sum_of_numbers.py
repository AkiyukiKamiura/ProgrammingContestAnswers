#! python3
# sum_of_numbers.py

while True:
    x = input()
    if x == '0': break

    sum = 0
    for c in x:
        sum += int(c)
    print(sum)
