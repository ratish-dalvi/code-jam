"""
Skeleton to solve problems
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    R, C = map(int, f.readline().strip().split(" "))

    # integer lists
    arr = np.array([list(f.readline().strip()) for i in range(R)])
    ii = 0
    d = {ii: []}
    for i in range(R):
        for j in range(C):
            if arr[i][j] != '?':
                if i > ii:
                    ii = i
                    d[ii] = [j]
                else:
                    d[ii].append(j)
    prev_i = 0
    if len(d[0]) == 0:
        del d[0]
    keys = sorted(d.keys())
    for i in keys:
        prev_j = 0
        for j in d[i]:
            next_i = R if i == keys[-1] else i+1
            next_j = C if j == d[i][-1] else j+1
            arr[prev_i: next_i, prev_j: next_j] = arr[i][j]
            prev_j = j+1
        arr[prev_i: i+1, prev_j:] = arr[i][j]
        prev_i = i+1
    arr[prev_i:, prev_j:] = arr[i][j]

    print("Case #%d:" % (c+1))
    for i in range(R):
        print "".join(arr[i])

f.close()
