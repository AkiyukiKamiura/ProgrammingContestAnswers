#! python3
# coding: utf-8

# TODO: やり直し

N = int(input())
presenters = [input().split(' ') for i in range(N)]

starttime = 600
lunch_break = False
for i in range(N):
    person, time = presenters[i]
    time = int(time)
    if i != 0:
        if lunch_break == False and starttime + time + 10 >= 720:
            starttime += 60
            lunch_break = True
        else:
            starttime += 10
    endtime = starttime + time
    print("%02d:%02d - %02d:%02d %s"%(int(starttime/60), starttime%60, int(endtime/60), endtime%60, person))
    starttime = endtime
