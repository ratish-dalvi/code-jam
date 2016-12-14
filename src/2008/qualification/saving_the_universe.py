"""
https://code.google.com/codejam/contest/32013/dashboard

Greedy Approach
---------------
1. Switch when all distinct elements at least occur once
2. Reset and Repeat 1 till the end.
"""

import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    # read
    S = int(f.readline().strip())
    engines = [f.readline().strip() for i in range(S)]
    Q = int(f.readline().strip())

    set_e = set([])
    out = 0
    for i in range(Q):
        q = f.readline().strip()
        set_e.add(q)
        if len(set_e) == S:
            out += 1
            set_e = set([q])
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
