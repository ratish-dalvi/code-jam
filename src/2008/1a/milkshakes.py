"""
Type: Boolean Satisfiability Problem.
The restriction "at most one unmalted per customer" makes this solvable.
 -> Start with all 0s (unmalted)
 -> Only one way movement is poosible from 0 -> 1
 -> Unsatisfied customer having any '1' -- convert to 1
 -> Unsatisfied customer with all 0s -- return impossible

Complexity: Amortised O(n)
"""

import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from queue import Queue

f = open(sys.argv[1])

C = int(f.readline().strip())
for ii in range(C):
    N = int(f.readline().strip())  # n_milshakes
    M = int(f.readline().strip())  # n_customers
    # Customer preferences: [(n_zeroes, milkshake_index_of_one), ...]
    c_prefs = [[0, -1] for j in range(M)]
    # Milkshake preferences: {milkshake_index: [cust_index1, cust_index2, ..]}
    m_prefs = [set([]) for j in range(N)]  # Starts with 1
    batch = [0] * N
    q = Queue()  # Queue of Unsatisfied
    sat_ones = set([])  # Set of satisfied ones

    for cc in range(M):
        tmp = map(int, f.readline().strip().split(" "))
        for j in range(tmp[0]):
            mi, fl = tmp[j*2 + 1] - 1, tmp[j*2 + 2]  # milkshake_index, flavour
            m_prefs[mi].add(cc)
            if fl == 0:
                c_prefs[cc][0] += 1
            elif fl == 1:
                c_prefs[cc][1] = mi
        if c_prefs[cc][0] == 0:  # Unsatisfied
            q.add(cc)

    while not q.isEmpty():
        cc = q.remove()  # unsatisfied customer
        batch[c_prefs[cc][1]] = 1
        sat_ones.add(cc)  # satisfied
        for kk in m_prefs[c_prefs[cc][1]]:
            if kk in sat_ones:  # Customer kk already satisfied
                continue
            if c_prefs[kk][1] != -1:  # Customer contains One
                if c_prefs[kk][1] == c_prefs[cc][1]:  # One exists at the pos
                    sat_ones.add(kk)
                elif c_prefs[kk][0] == 1:  # exactly 'One' and 'Zero'
                    q.add(kk)  # Add to queue
            elif c_prefs[kk][0] == 1:  # If just one 'zero'
                batch = "IMPOSSIBLE"
                q.remove_all()
                break
            c_prefs[kk][0] -= 1
    batch = " ".join(map(str, batch)) if isinstance(batch, list) else batch
    print("Case #%d: %s" % (ii+1, batch))

f.close()
