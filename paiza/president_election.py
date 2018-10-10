#! python3
# coding: utf-8

M = int(input())
candidates = {}
candidate_republican = {}
candidate_democratic = {}
for i in range(M):
    party = input()
    candidates[i+1] = party
    if party == 'Republican':
        candidate_republican[i+1] = 0
    elif party == 'Democratic':
        candidate_democratic[i+1] = 0

N = int(input())
voters = [list(map(int, input().split(' '))) for n in range(N)]

preliminary_points = [0 for i in range(M)]
for priority in voters:
    rep_flag = False
    dem_flag = False
    for can in priority:
        if candidates[can] == 'Republican' and rep_flag == False:
            candidate_republican[can] += 1
            rep_flag = True
        if candidates[can] == 'Democratic' and dem_flag == False:
            candidate_democratic[can] += 1
            dem_flag = True
        if rep_flag == True and dem_flag == True: break

final_candidates = {max(candidate_republican, key=candidate_republican.get): 0,
                    max(candidate_democratic, key=candidate_democratic.get): 0}

for priority in voters:
    for can in priority:
        if can in final_candidates:
            final_candidates[can] += 1
            break

print(max(final_candidates, key=final_candidates.get))
