"""
https://code.google.com/codejam/contest/544101/dashboard#s=p0&a=0

1. Shift to the right instead of rotating
2. Since the maximum value of N is only 50, I chose a simple and readable
   algorithm for finding whether a player has K pieces joined -- Start from
   top-left and for every element, check k elements on east, south,
   south-east diagonal and south-west diagonal.
Large finishes in under a second.
"""
import sys
import numpy as np

f = open(sys.argv[1])

T = int(f.readline().strip())
for cc in range(T):
    N, K = map(int, f.readline().strip().split(" "))
    lst = []
    for i in range(N):
        lst.append(list(f.readline().strip()))
    arr = np.array(lst)

    # rotate / Shift right
    for i in range(N):
        k = 0
        for j in reversed(range(N)):
            if arr[i][j] != '.':
                if j != N-1-k:
                    arr[i][N-1-k] = arr[i][j]
                    arr[i][j] = '.'
                k += 1
    # count
    won = {"R": False, "B": False}
    out = {"R": "Red", "B": "Blue", "": "Neither", "BR": "Both", "RB": "Both"}

    for i in range(N):
        for j in reversed(range(N)):
            if arr[i][j] != '.' and not won[arr[i][j]]:
                a = b = c = d = 0
                for k in range(K):  # horizontal
                    a += (j+k < N and arr[i][j+k] == arr[i][j])
                    b += (i+k < N and arr[i+k][j] == arr[i][j])
                    c += (i+k < N and j+k < N and arr[i+k][j+k] == arr[i][j])
                    d += (i+k < N and j-k >= 0 and arr[i+k][j-k] == arr[i][j])
                won[arr[i][j]] = (a == K or b == K or c == K or d == K)
        if sum(won.values()) == 2:
            break
    o = out["".join([k for k, v in won.iteritems() if v])]
    print("Case #%d: %s" % (cc+1, o))

f.close()
