"""
https://code.google.com/codejam/contest/1645485/dashboard
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    A, B = map(int, f.readline().strip().split(" "))
    probs = map(float, f.readline().strip().split(" "))
    cum_probs = [0]*(A + 1)
    p = 1
    for i, x in enumerate(probs):
        p = p * x
        cum_probs[i+1] = p

    min_ee = np.inf
    for i in range(A):
        ee = (cum_probs[A-i]) * (B - A + 2*i + 1) + \
             (1 - cum_probs[A-i]) * (B - A + 2*i + 1 + B + 1)
        min_ee = min(min_ee, ee)
    min_ee = min(min_ee, B + 2)

    print("Case #%d: %.6f" % (c+1, min_ee))

f.close()
