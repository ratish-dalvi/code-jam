"""
Skeleton to solve problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    n = int(f.readline().strip())

    # integer lists
    # v1 = map(int, f.readline().strip().split(" "))
    # v2 = map(int, f.readline().strip().split(" "))

    # Write algorithm here
    out = None
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
