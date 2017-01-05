"""
https://code.google.com/codejam/contest/635101/dashboard#s=p1
"""
import sys

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    N, K, B, T = map(int, f.readline().strip().split(" "))
    pos = map(int, f.readline().strip().split(" "))
    vel = map(int, f.readline().strip().split(" "))
    sloths = swaps = k = 0
    out = "IMPOSSIBLE"
    for i in reversed(range(N)):
        if pos[i] + (vel[i] * T) < B:
            sloths += 1
        else:
            swaps += sloths
            k += 1
        if k == K:
            out = swaps
            break
    print("Case #%d: %s" % (c+1, str(out)))
f.close()
