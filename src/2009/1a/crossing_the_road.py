"""
https://code.google.com/codejam/contest/188266/dashboard#s=p1&a=0
Dijkstra's Algorithm:

Graph Implemented by using a 2D numpy array with values as edge weights / times
Ideally, Priority Queue should have been used to choose the min node. But
the grid in the large set is 20*20 at most, which gives n <= 20*20*4 (a small
number to allow quadratic complexity) -- where n is the number of nodes in the
graph of this implementation. So, I just used simple sequential min().
It finishes in about half a second on the large dataset.
"""
import os
import numpy as np
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from utils import np_argmin
f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    n, m = map(int, f.readline().strip().split(" "))
    tts = []  # n, m, 3 (ith intersection from north, jth from west)
    for i in range(n):
        tts.append(map(int, f.readline().strip().split(" ")))

    # initialize
    wait_times = np.reshape(tts, (n, m, 3))
    dist = np.ones((2*n, 2*m)) * np.inf  # Empty Graph
    visited = np.zeros(dist.shape)  # 0 is False, np.inf is True

    def neighbours(x, y):
        return [(i, j) for i, j in
                ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1))
                if i >= 0 and i < dist.shape[0]
                and j >= 0 and j < dist.shape[1]]

    x_, y_ = (0, 0)  # coordinates of the current node
    end = (2*n-1, 2*m-1)  # Ending node in the graph search
    dist[0][0] = 0  # Start with (0, 0)

    while (x_, y_) != end:
        s, w, t_cyc = wait_times[n - 1 - x_/2][y_/2]
        t_curr = dist[x_][y_]
        for (x, y) in neighbours(x_, y_):
            offset = (t_curr - t_cyc) % int(s + w)
            if (x/2 - x_/2) or (y/2 - y_/2):
                t = 2
            elif (x - x_):
                t = s + w - offset + 1 if offset + 1 > s else 1
            elif (y - y_):
                t = s - offset + 1 if offset < s else 1
            if t + t_curr < dist[x][y]:
                dist[x][y] = t + t_curr
        visited[x_][y_] = np.inf
        x_, y_ = np_argmin(visited + dist)
    print("Case #%d: %d" % (c+1, dist[x_][y_]))

f.close()
