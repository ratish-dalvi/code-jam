"""
https://code.google.com/codejam/contest/3264486/dashboard#s=p2
"""
import os
import sys
import math
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


def num_odd_evens(x, depth):
    n_odd = n_even = 0
    if x % 2:
        n_odd = 1
    else:
        n_even = 1
    lst = [x]
    for i in range(depth):
        lst_new = set([])
        # count descendents from evens
        tmp_n_odd = tmp_n_even = n_even
        for y in lst:
            lst_new.update(set([(y-1)//2, (y-1) - (y-1)//2]))
            # count descendents from odds
            if y % 2:
                if (y//2) % 2:  # if divided by 2 is odd
                    tmp_n_odd += 2 * n_odd
                else:
                    tmp_n_even += 2 * n_odd
        n_odd = tmp_n_odd
        n_even = tmp_n_even
        lst = list(lst_new)
    return lst, n_even, n_odd

T = int(f.readline().strip())
for c in range(T):
    n, k = map(int, f.readline().strip().split(" "))
    # Write algorithm here
    last_level = int(math.floor(math.log(k, 2)))
    n_last_level = k - (2**last_level - 1)
    lst, n_even, n_odd = num_odd_evens(n, last_level)
    m = max(lst)
    if m % 2:  # odd
        num = max(lst) if n_last_level <= n_odd else min(lst)
    else:
        num = max(lst) if n_last_level <= n_even else min(lst)
    out = [(num-1) - (num-1)//2, (num-1)//2]
    print("Case #%d: %s %s" % (c+1, out[0], out[1]))

f.close()
