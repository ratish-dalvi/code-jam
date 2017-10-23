"""
https://code.google.com/codejam/contest/1836486/dashboard#s=p1
"""
import os
import sys
import numpy as np

sys.path.append(os.path.abspath('./src/helpers'))
from utils import np_argmin

f = open(sys.argv[1])
infinite = np.inf


def travel_time(p1, p2, t_curr, water_drop):
    c1, c2, f1, f2 = X_ceil[p1], X_ceil[p2], X_floor[p1], X_floor[p2]
    if water_drop:
        h = max(0, H - (t_curr * 10.0))
        t1 = (0 if (min(c1, c2) - max(f1, f2) >= 50) else infinite)
        t2 = max(0, ((50 - (c2 - h)) / 10.0))  # wait time
        t3 = 1 if ((h - t2*10) - f1) >= 20 else 10  # passing through
        t = t_curr + t1 + t2 + t3  # Total
    else:
        t = (0 if (min(c1, c2) - max(f1, f2, H) >= 50) else infinite)
    return t


def try_to_get_out(time, water_drop):
    if time[N-1, M-1] != infinite:
        return time[N-1, M-1]
    visited = np.zeros((N, M))  # infinite - True, 0 - False
    node = (0, 0)
    value = 0.0
    while (value != infinite):
        for new_node in neighbours(node):
            new_time = travel_time(node, new_node, time[node], water_drop)
            if new_time < time[new_node]:
                time[new_node] = new_time
        visited[node] = infinite
        node, value = np_argmin(visited + time, lean=False)
    return time[N-1, M-1]


def neighbours((i, j)):
    out = []
    if i > 0:
        out.append((i-1, j))
    if i < N-1:
        out.append((i+1, j))
    if j > 0:
        out.append((i, j-1))
    if j < M-1:
        out.append((i, j+1))
    return out


T = int(f.readline().strip())
for c in range(T):
    # Read the input
    H, N, M = map(int, f.readline().strip().split(" "))
    X_ceil = np.array(
        [map(int, f.readline().strip().split(" ")) for i in range(N)])
    X_floor = np.array(
        [map(int, f.readline().strip().split(" ")) for i in range(N)])

    X_time = np.ones((N, M)) * infinite  # Empty Graph
    X_time[(0, 0)] = 0.0  # Guaranteed to be reachable

    # Start Kayaking :)
    out_time = try_to_get_out(X_time, water_drop=False)
    out_time = try_to_get_out(X_time, water_drop=True)

    print("Case #%d: %s" % (c+1, str(out_time)))

f.close()
