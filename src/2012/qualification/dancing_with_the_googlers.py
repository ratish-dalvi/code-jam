"""
https://code.google.com/codejam/contest/1460488/dashboard#s=p1
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

mapping = [
    [0, 1],
    [1, 1],
    [1, 2]
]
T = int(f.readline().strip())
for c in range(T):
    inp = map(int, f.readline().strip().split(" "))
    N, S, p, lst = inp[0], inp[1], inp[2], inp[3:]
    ns = ss = ts = 0  # Not suprising above p, surprsing above p
    for x in lst:
        y = x % 3
        ns += ((x/3) + min(x, mapping[y][0])) >= p
        ss += ((x/3) + min(x, mapping[y][1])) >= p
        ts += (x >= 2)
    out = 0 if S > ts else (ns + min(ss-ns, S))
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
