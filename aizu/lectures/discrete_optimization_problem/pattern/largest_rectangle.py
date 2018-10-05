#! python3
# largest_rectangle.py

H, W = list(map(int, input().split(' ')))
tiles = [list(map(int, input().split(' '))) for i in range(H)]

table = [[0 for j in range(W)] for i in range(H)]
