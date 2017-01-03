"""
https://code.google.com/codejam/contest/544101/dashboard#s=p1&a=1

Type - Dynamic Programming

Small - 21 seconds
large - 16 minutes :(

Complexity - O(256 * 256 * n)
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])
T = int(f.readline().strip())

inf = 9999999  # can't use np.inf since I want to multiply with 0
for c in range(T):
    D, I, M, N = map(int, f.readline().strip().split(" "))
    cache = np.ones((N, 256)) * -1
    pixels = map(int, f.readline().strip().split(" "))
    out = np.inf

    def go(pixels, n, y):  # y is the current pixel value
        if n == -1:
            return 0
        if cache[n][y] != -1:
            return cache[n][y]
        best = go(pixels, n-1, y) + D
        for x in range(256):  # previous pixel value
            o = go(pixels, n-1, x)
            best = min(
                best,
                o + abs(y - pixels[n]) +
                (((max(0, abs(y - x) - 1) // max(M, 1)) * I)
                 if M > 0 else inf*(abs(y-x))))
        cache[n][y] = best
        return best

    for j in range(256):
        out = min(out, go(pixels, N-1, j))
    print("Case #%d: %d" % (c+1, int(out)))

f.close()
