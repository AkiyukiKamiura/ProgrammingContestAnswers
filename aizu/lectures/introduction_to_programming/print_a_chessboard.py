#! python3
# print_a_chessboard.py

while True:
    H, W = [int(x) for x in input().split(' ')]
    if H == 0 and W == 0: break

    for i in range(H):
        row = ''
        for j in range(W):
            if ((i%2) + (j%2))%2:
                row += '.'
            else:
                row += '#'
        print(row)
    print('')
