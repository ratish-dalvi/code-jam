
"""
Problem Solved using undirected graph
-------------------------------------

1. Find Prime numbers from P till N where N = min(B/2, B - A)
   A prime number larger than B - A will not have two multiple within
   the interval. This is important because the prime number algorithm
   wouldn't finish within the given time for P ~ 10^12.
2. For each prime number, find it's multiples in interval A, B
3. Create a graph consisting of numbers in the interval as nodes and
   common prime factors as edges
4. Find disjoint sets in the Graph

Note - The program takes about 4-5 minutes. Although the implementation uses a
    linear solution to find the disconnected components, python slows it
    down :(. Prime number generation alone takes up about 1 minute for all
    the inputs of the large dataset.
"""

import os
import sys
import math
sys.path.append(os.path.abspath('./src/helpers'))
from utils import prime_numbers
from graphs import Graph

f = open(sys.argv[1])

T = int(f.readline().strip())
for cc in range(T):
    # integer lists
    A, B, P = map(int, f.readline().strip().split(" "))
    p_nums = prime_numbers(min(B/2 + 1, B - A)) - set(range(P))
    g = Graph(range(A, B+1))
    for i in p_nums:
        start = int(i*(math.ceil(A/float(i))))
        for j in range(start + i, B+1, i):
            g.add_unidrected_edge(start, j)
    print("Case #%d: %s" % (cc+1, str(g.num_connected_components())))
f.close()
