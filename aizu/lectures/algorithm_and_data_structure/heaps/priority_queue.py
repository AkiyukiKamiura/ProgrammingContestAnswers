#! python3
# priority_queue.py

import sys
from heapq import heappush, heappop

# わからん
pq = []
lines = sys.stdin.readlines()
for line in lines:
    op = line.strip().split(' ')
    if op[0] == 'insert':
        heappush(pq, -int(op[1]))
    elif op[0] == 'extract':
        print(-heappop(pq))
    else:
        break

# import sys, time
#
# class PriorityQueue:
#     __slots__ = ['nodes', 'num']
#
#     def __init__(self):
#         self.nodes = []
#         self.num = 0
#
#     def max_heapify(self, i):
#         if i >= self.num: return
#         left, right = (i+1)*2-1, (i+1)*2
#
#         largest = i
#         if left < self.num and self.nodes[i] < self.nodes[left]: largest = left
#         if right < self.num and self.nodes[largest] < self.nodes[right]: largest = right
#
#         if largest != i:
#             self.nodes[i], self.nodes[largest] = self.nodes[largest], self.nodes[i]
#             self.max_heapify(largest)
#
#     def extract_max(self):
#         if self.num < 1: return
#         max = self.nodes[0]
#         self.nodes[0] = self.nodes[-1]
#         self.nodes.pop()
#         self.num -= 1
#         self.max_heapify(0)
#         return max
#
#     def insert(self, key):
#         self.nodes.append(key)
#         self.num += 1
#         i = self.num-1
#         par = lambda i: (i-1)//2
#         while i > 0 and self.nodes[par(i)] < self.nodes[i]:
#             self.nodes[i], self.nodes[par(i)] = self.nodes[par(i)], self.nodes[i]
#             i = par(i)
#
#     def print_element(self):
#         for node in self.nodes:
#             print('', node, end='')
#         print('')
#
# pq = PriorityQueue()
#
# start = time.time()
# lines = sys.stdin.readlines()
# for line in lines:
#     op = line.strip().split(' ')
#     if op[0] == 'insert':
#         pq.insert(int(op[1]))
#     elif op[0] == 'extract':
#         # print(pq.extract_max())
#         pq.extract_max()
#     else:
#         break
# print('elapsed:', time.time()-start)
