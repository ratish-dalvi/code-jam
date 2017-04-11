"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p3
"""
import sys
import numpy as np

f = open(sys.argv[1])


def get_diagonals(ii, jj, N):
    for i in range(N):
        for j in range(jj, N):
            if

T = int(f.readline().strip())
for c in range(T):
    print "Case %d" % (c + 1)
    # Read data
    N, M = map(int, f.readline().strip().split(" "))
    arr = [['.' for i in range(N)] for j in range(N)]
    allowed = [[set(['+', 'x', 'o']) for i in range(N)] for j in range(N)]
    for i in range(M):
        val, x, y = f.readline().strip().split(" ")
        arr[int(x)-1][int(y)-1] = val

    # Algorithm starts here
    # Compute allowed entries based on the present models in arr
    if c == 2:
        arr[0][1] = '?'
    print np.array(arr)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '+':
                # Get all 4 diagonals
                for ii in range(i, N):
                    for jj in range(j, N):
                        if "o" in allowed[ii][jj]:
                            allowed[ii][jj]
                        if "o" in allowed[ii][jj].remove("o")

    out = None
    # print np.array(allowed)
    # print("Case #%d: %s" % (c+1, str(out)))

f.close()
