"""
https://code.google.com/codejam/contest/32017/dashboard#s=p1

Problem Solved using Union-find
-------------------------------------

1. Find Prime numbers from P till N where N = min(B/2, B - A)
   A prime number larger than B - A will not have two multiple within
   the interval. This is important because the prime number algorithm
   wouldn't finish within the given time for P ~ 10^12.
2. For each prime number, find it's multiples in interval A, B
3. Create a graph consisting of numbers in the interval as nodes and
   common prime factors as edges
4. Find disjoint sets in the Graph

Note - Comparison between Union-find and Undirected-graph on large Dataset:
       UnionFind - 6m 14s
       Undirected Graph - 5m37s

"""

import os
import sys
import math
sys.path.append(os.path.abspath('./src/helpers'))
from utils import prime_numbers
from union_find import UnionFind

f = open(sys.argv[1])

T = int(f.readline().strip())
for cc in range(T):
    # integer lists
    A, B, P = map(int, f.readline().strip().split(" "))
    p_nums = prime_numbers(min(B/2 + 1, B - A)) - set(range(P))
    uf = UnionFind()
    for i in p_nums:
        start = int(i*(math.ceil(A/float(i))))
        for j in range(start + i, B+1, i):
            uf.union(start, j)
    out = (B - A + 1 - uf.number_of_items() + uf.number_of_roots())
    print("Case #%d: %s" % (cc+1, str(out)))
f.close()
