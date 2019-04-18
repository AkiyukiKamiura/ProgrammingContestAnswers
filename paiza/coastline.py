# coding: utf-8

from collections import deque

H, W = list(map(int, input().split(' ')))
map = [['.' for i in range(W+2)] for j in range(H+2)]
for i in range(H):
    tmp = list(input())
    for j in range(len(tmp)):
        map[i+1][j+1] = tmp[j]

islands = []
check_map = [[False for j in range(W+2)] for i in range(H+2)]
for h in range(1, H+1):
    for w in range(1, W+1):
        if check_map[h][w] == True: continue
        check_map[h][w] = True
        if map[h][w] == '#':
            queue = deque()
            queue.append((h, w))
            check_map[h][w] = True
            island = {'upper_left_point': (h, w), 'square': 0, 'coastline': 0}
            while len(queue) != 0:
                hc, wc = queue.popleft()
                island['square'] += 1
                for hs, ws in [(hc-1, wc), (hc+1, wc), (hc, wc-1), (hc, wc+1)]:
                    if map[hs][ws] == '#':
                        if check_map[hs][ws] != True:
                            queue.append((hs, ws))
                            check_map[hs][ws] = True
                    else:
                        island['coastline'] += 1
            islands.append(island)

islands = sorted(islands, key=lambda x: (x['square'], x['coastline']), reverse=True)
for island in islands:
    print(island['square'], island['coastline'])
