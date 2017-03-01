"""
https://code.google.com/codejam/contest/1150485/dashboard#s=p1

Each pair of vendors i,j must move far enough from each other for the vendors
in between them to fit in. So, they need to have at least D*(i - j) space
between them i.e move Y_ij = D*(i - j) - (x_i - x_j) distance apart.
It can easily be shown that this 'max' distance can move at 2 m/s.
so the answer would be to compute: max(Y_ij) / 2.
This can be computed in linear time by decomposing it into
maximum_contiguous_subarray problem and solving using Kadane's algorithm.
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from utils import maximum_contiguous_subarray

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    C, D = map(int, f.readline().strip().split(" "))
    lst = []
    prev_p = None
    for i in range(C):
        P, V = map(int, f.readline().strip().split(" "))
        for i in range(V):
            if prev_p is not None:
                lst.append(D - (P - prev_p))
            prev_p = P
    print("Case #%d: %.1f" % (c+1, maximum_contiguous_subarray(lst) / 2.0))

f.close()
