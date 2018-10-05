#! python3
# print_a_rectangle.py

while True:
    H, W = [int(x) for x in input().split(' ')]
    if H == 0 and W == 0: break

    for i in range(H):
        print('#'*W)

    print('')
