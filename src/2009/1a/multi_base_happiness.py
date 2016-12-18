"""
https://code.google.com/codejam/contest/188266/dashboard#s=p0&a=0
1. Happy numbers reach cycles -
   https://en.wikipedia.org/wiki/Happy_number#Programming_example
2. Use caching to improve speed.
3. Higher bases converge quickly. So, reverse sort input bases

Large input finishes in 3 minutes.
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from math_utils import is_happy_number
f = open(sys.argv[1])


T = int(f.readline().strip())
cache = [{} for i in range(11)]  # 1 for each base
for c in range(T):
    # integer lists
    bases = sorted(map(int, f.readline().strip().split(" ")), reverse=True)
    n = 2
    while True:
        for b in bases:
            y = cache[b].get(n)
            if y is None:
                y, numbers = is_happy_number(n, b)
                for i in numbers:
                    cache[b][i] = y
            if not y:
                break
        if b == bases[-1] and y is True:
            break
        n += 1
    print("Case #%d: %d" % (c+1, n))

f.close()
