#! python3
# print_test_cases.py

for i in range(10000):
    x = int(input())
    if x == 0:
        break
    print('Case ' + str(i+1) + ': ' + str(x))
