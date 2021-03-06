# coding: utf-8

H, W = list(map(int, input().split(' ')))
intersections = [list(map(int, input().split(' '))) for i in range(H)]

min_score = float('inf')
for h in range(H):
    for w in range(W):
        score = 0
        not_min_flag = False
        for _h in range(H):
            if _h == h: continue
            for _w in range(W):
                if _w == w: continue
                score += intersections[_h][_w] * min(abs(h - _h), abs(w - _w))
                if score > min_score:
                    not_min_flag = True
                    break
            if not_min_flag: break
        if score < min_score: min_score = score

print(min_score)
