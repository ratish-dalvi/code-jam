"""
https://code.google.com/codejam/contest/1836486/dashboard
let sum x_i = X  where x_i is the ith element and p is the minimum required
fraction for the ith element to not be eliminated.
The main idea is to match (xi + pX) with [(X - xi) + (1 - p)X] / (n-1)
But the first term (X - xi) isn't right. If there are elements which can never
be 'matched' we should remove them from X. So, we start from the highest
element in the decreasing order and if p < 0 (it can't be matched) we remove
it from X for the subsequent elements.
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    lst = map(int, f.readline().strip().split(" "))
    N, ss = lst[0], np.array(lst[1:])
    X_ = X = sum(ss)
    out = [0]*N
    order = np.argsort(ss)[::-1]  # reverse sort indices
    for i in order:
        out[i] = max(0, 100.0*(X_ + X - N*ss[i])/(X*N))
        if out[i] == 0:
            N -= 1
            X_ = X_ - ss[i]
    print("Case #%d: %s" % (c+1, " ".join(map(str, out))))
f.close()
