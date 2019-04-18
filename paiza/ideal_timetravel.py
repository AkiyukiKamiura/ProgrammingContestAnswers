#! python3
# coding: utf-8

# 深さ優先探索
# 枝切りする

from collections import deque

N = int(input())
c_f, c_b = list(map(int, input().split(' ')))
start_state = input()

queue = deque([{'route': str(N), 'state': start_state, 'cost': 0}])
min_cost = float('inf')
min_route = ''
while len(queue) != 0:
    routes = queue.popleft()
    history, state, cost = routes['route'], routes['state'], routes['cost']
    now_era = int(history[-1])

    for i in range(1, N+1): # 先
        if state[i-1] == 'd' or i == now_era: continue
        new_cost = cost
        if i < now_era: new_cost += c_b
        elif now_era < i: new_cost += c_f
        if min_cost <= new_cost: continue

        new_state = ''
        for j in range(1, len(state)+1):
            if j <= i: new_state += state[j-1]
            else:
                if state[j-1] == 's': new_state += 'd'
                else: new_state += 's'

        new_route = {'route': history + str(i), 'state': new_state, 'cost': new_cost}
        if i == N and len(set(new_route['route'])) == N:
            if new_route['cost'] < min_cost:
                min_cost = new_route['cost']
                min_route = new_route['route']
        else:
            queue.append(new_route)

print(' '.join(list(map(str, min_route))))
