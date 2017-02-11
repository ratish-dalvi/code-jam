"""
http://code.google.com/codejam/contest/1150485/dashboard
"""
import sys
import numpy as np

f = open(sys.argv[1])


def score(lst):
    x = [int(i) for i in lst if i != "."]
    return float(sum(x)) / len(x)


T = int(f.readline().strip())
for c in range(T):
    N = int(f.readline().strip())
    # integer lists
    wp = [0]*N
    owp = [0]*N
    rpi = [0]*N
    arr = [list(f.readline().strip()) for i in range(N)]
    for i in range(N):
        wp[i] = score(arr[i])
        owp[i] = np.mean([score(arr[j][:i] + arr[j][i+1:])
                          for j in range(N) if arr[j][i] != "."])
    for i in range(N):
        oowp = np.mean([owp[j] for j in range(N) if arr[i][j] != "."])
        rpi[i] = 0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp

    print("Case #%d:" % (c+1))
    for i in range(N):
        print(rpi[i])

f.close()
