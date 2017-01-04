"""
https://code.google.com/codejam/contest/544101/dashboard#s=p1&a=1

Type - Dynamic Programming

This is a bottom-up iterative implementation of the recursive algorithm
without directly using memoization. We do store the results in a 1X256 array
which is updated at every step.

Complexity - O(256 * 256 * n)
Time:
Small - 13 seconds
Large - 8m 14 seconds
"""
import sys

f = open(sys.argv[1])
T = int(f.readline().strip())

inf = 99999999  # can't use np.inf since I want to multiply with 0
for c in range(T):
    D, I, M, N = map(int, f.readline().strip().split(" "))
    pixels = map(int, f.readline().strip().split(" "))
    arr1 = [0] * 256
    for p in pixels:
        arr2 = map(lambda x: x + D, arr1)  # Deleting cost
        for x in range(256):  # previous pixel
            for y in range(256):  # current pixel
                arr2[y] = min(arr2[y], arr1[x] + abs(p - y) +
                              (((max(0, abs(y - x) - 1) // max(M, 1)) * I)
                               if M > 0 else abs(y-x) * inf))
        arr1 = arr2
    print("Case #%d: %d" % (c+1, min(arr1)))
f.close()
