#! python3
# structured_programming.py

n = int(input())

for i in range(1, n+1):
    if i%3 == 0:
        print(' ' + str(i), end='')
    else:
        x = i
        while x != 0:
            if x%10 == 3:
                print(' ' + str(i), end='')
                break
            x = int(x/10)
print('')
