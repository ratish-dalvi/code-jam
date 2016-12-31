"""
https://code.google.com/codejam/contest/90101/dashboard#s=p1&a=3
Used Union-Find Data Structure
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))
from union_find import UnionFind


f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    uf = UnionFind()
    H, W = map(int, f.readline().strip().split(" "))
    arr = np.zeros((H, W))
    for i in range(H):
        for j, x in enumerate(map(int, f.readline().strip().split(" "))):
            arr[i][j] = x

    for i in range(H):
        for j in range(W):
            neighbours = [
                (x, y) for (x, y) in ((i-1, j), (i, j-1), (i, j+1), (i+1, j))
                if x >= 0 and x < H and y >= 0 and y < W]
            min_a, min_b = i, j
            for (x, y) in neighbours:
                if arr[x][y] < arr[min_a][min_b]:
                    min_a, min_b = x, y
            if (min_a, min_b) != (i, j):
                uf.union("%d_%d" % (i, j), "%d_%d" % (min_a, min_b))

    tmp = {}
    print("Case #%d:" % (c+1))
    for i in range(H):
        out = []
        for j in range(W):
            x = uf["%d_%d" % (i, j)]
            tmp[x] = tmp.get(x, chr(97 + len(tmp)))
            out.append(tmp[x])
        print " ".join(out)
f.close()
