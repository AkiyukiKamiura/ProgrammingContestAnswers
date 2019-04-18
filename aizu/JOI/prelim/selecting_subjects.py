# coding: utf-8

science = [int(input()) for i in range(4)]
society = [int(input()) for i in range(2)]

score = 0
score += max(society)
score += sum(science) - min(science)
print(score)
