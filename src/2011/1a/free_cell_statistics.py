"""
Skeleton to solve the problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from math_utils import gcd

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    N, Pd, Pg = map(int, f.readline().strip().split(" "))
    if Pg == 0 or Pg == 100:
        out = "Possible" if Pd == Pg else "Broken"
    elif Pd == 0:
        out = "Possible"
    else:
        out = "Possible" if (100 / gcd(Pd, 100)) <= N else "Broken"
    print("Case #%d: %s" % (c+1, str(out)))
f.close()
