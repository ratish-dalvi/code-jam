"""
Skeleton to solve problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    lst = map(int, f.readline().strip().split(" "))
    N, ss = lst[0], lst[1:]
    print N, ss
    # Write algorithm here
    out = None
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
