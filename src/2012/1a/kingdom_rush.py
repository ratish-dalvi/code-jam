"""
https://code.google.com/codejam/contest/1645485/dashboard#s=p1

Sort level 2 and traverse in the ascending order.
for each level check if you have enough points, if not try solving level 1 in
the descending order of level 2 -- this is because we want to avoid doing a
level twice if we can.
"""
import sys
import numpy as np

f = open(sys.argv[1])


def alg():
    asort2 = arr[:, 1].argsort()
    pts = i = 0
    while i < N:
        j = N - 1
        while pts < arr[asort2[i], 1]:
            if j == i - 1:
                return "Too Bad"
            if pts >= arr[asort2[j], 0] and arr[asort2[j], 2] == 0:
                pts += 1
                arr[asort2[j], 2] += 1
                j = N
            j -= 1
        pts += 2 - arr[asort2[i], 2]
        arr[asort2[i], 2] += 1
        i += 1
    return arr[:, 2].sum()

T = int(f.readline().strip())
for c in range(T):
    N = int(f.readline().strip())
    # points for level 1, points for level 2, num attempts at this level
    arr = np.array(
        [map(int, f.readline().strip().split(" ")) + [0] for i in range(N)])
    print("Case #%d: %s" % (c+1, alg()))

f.close()
