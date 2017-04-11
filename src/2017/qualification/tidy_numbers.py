"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p1
"""
import os
import sys

sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


T = int(f.readline().strip())
for c in range(T):
    lst = map(int, list(f.readline().strip()))
    n = len(lst)
    for i in reversed(range(n-1)):
        if lst[i] > lst[i+1]:
            lst[i] -= 1
            j = i + 1
            while j < n:
                lst[j] = 9
                j += 1
        if i == 0 and lst[i] <= 0:
            lst = lst[1:]
    print("Case #%d: %s" % (c+1, "".join(map(str, lst))))

f.close()
