#! python3
# print_a_frame.py

while True:
    H, W = [int(x) for x in input().split(' ')]
    if H == 0 and W == 0: break

    for i in range(H):
        if i == 0 or i == H-1:
            print('#'*W)
        else:
            print('#' + '.'*(W-2) + '#')

    print('')
