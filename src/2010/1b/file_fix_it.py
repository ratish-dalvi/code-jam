"""
https://code.google.com/codejam/contest/635101/dashboard
"""
"""
Skeleton to solve the problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    N, M = map(int, f.readline().strip().split(" "))
    existing = set([f.readline().strip() for i in range(N)])
    cnt = 0
    for i in range(M):
        y = ""
        for x in f.readline().strip().split("/")[1:]:
            y += "/" + x
            if y not in existing:
                cnt += 1
                existing.add(y)
    print("Case #%d: %s" % (c+1, str(cnt)))
f.close()
