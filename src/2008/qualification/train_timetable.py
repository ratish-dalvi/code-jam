"""
https://code.google.com/codejam/contest/32013/dashboard#s=p1

Greedy Approach
---------------
Data Structure used - Dict of time table for each station
  {
    0: [[], [X1], []] ... 1440 lists],   # 0 - A station
    1: [[]. [], [X2]] ... 1440 lists]    # 1 - B station
  }
Where X1 is the arrival time of a train departing from station 0 in
unit - minutes since midnight and index of X1 is the departure time
from that station in the same unit.
"""

import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


def format_time(x):
    y = x.split(":")
    return int(y[0]) * 60 + int(y[1])


def go(st, tt, w, tu):
    # start time, timetable, which - A(0), B(1), turnaround time
    for t in range(st, 1440):
        if len(tt[w][t]):  # has arrivals, add tu and send
            go(tt[w][t][0] + tu, tt, not w, tu)
            del tt[w][t][0]
            break

T = int(f.readline().strip())
for c in range(T):
    # fetch data
    tu = int(f.readline().strip())  # turnaround time
    na, nb = map(int, f.readline().strip().split(" "))
    ta = {0: [[] for i in range(1440)],
          1: [[] for i in range(1440)]}
    for i in range(na):
        st, end = f.readline().strip().split(" ")
        ta[0][format_time(st)].append(format_time(end))
    for i in range(nb):
        st, end = f.readline().strip().split(" ")
        ta[1][format_time(st)].append(format_time(end))

    # Algorithm
    a = b = 0
    for t in range(1440):  # for every minute
        for arr in ta[0][t]:
            go(arr + tu, ta, 1, tu)  # run train simulations from station A
            a += 1
        for arr in ta[1][t]:
            go(arr + tu, ta, 0, tu)  # run train simulations from station B
            b += 1
    print("Case #%d: %d %d" % (c+1, a, b))

f.close()
