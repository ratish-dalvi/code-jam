"""
https://code.google.com/codejam/contest/dashboard?c=32016#s=p0&a=1
"""
import sys
import numpy as np


f = open(sys.argv[1])
T = int(f.readline().strip())
for i in range(T):
    n = f.readline().strip()
    v1 = map(int, f.readline().strip().split(" "))
    v2 = map(int, f.readline().strip().split(" "))
    out = np.dot(sorted(v1), sorted(v2, reverse=True))
    print("Case #%d: %s\n" % (i+1, str(out)))

f.close()
