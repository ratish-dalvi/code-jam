"""
Skeleton to solve the problems
"""
import sys

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    N, K = map(int, f.readline().strip().split(" "))
    print("Case #%d: %s" % (c+1, "OFF" if (K + 1) % (2**N) else "ON"))

f.close()
