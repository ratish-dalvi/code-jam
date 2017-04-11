"""
https://code.google.com/codejam/contest/3264486/dashboard
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


def count_flips(lst, k, n):
    flip = 0
    for i, x in enumerate(lst):
        if x == '-':
            flip += 1
            for j in range(k):
                if i + j == n:
                    return "Impossible"
                else:
                    lst[i+j] = '+' if lst[i+j] == '-' else '-'
    return flip

T = int(f.readline().strip())
for c in range(T):
    lst, k = f.readline().strip().split(" ")
    lst = list(lst)
    k = int(k)
    n = len(lst)
    # Write the algorithm here
    out = count_flips(lst, k, n)
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
