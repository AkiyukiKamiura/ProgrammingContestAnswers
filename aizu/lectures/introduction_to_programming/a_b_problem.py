#! python3
# a_b_problem.py

a, b = [int(x) for x in input().split(' ')]
d = int(a/b)
r = a%b
f = a/b

print(d, r, "%.10f"%f)
