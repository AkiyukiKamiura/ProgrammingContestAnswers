#! python3
# coding: utf-8

n = int(input())
queries = [input() for i in range(n)]

stack = []
now_page = 'blank page'
for q in queries:
    if q.startswith('go to'):
        page = q[6:]
        stack.append(now_page)
        now_page = page
        print(now_page)
    elif q == 'use the back button':
        page = stack.pop()
        now_page = page
        print(page)
