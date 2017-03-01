"""
https://code.google.com/codejam/contest/975485/dashboard
"""
import sys

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    inp = f.readline().strip().split(" ")
    D = {'O': [0, 1], 'B': [0, 1]}  # Robot: [time_used_so_far, last_position]
    for i in range(int(inp[0])):
        robot = inp[2*i + 1]
        position = int(inp[2*i + 2])
        D[robot][0] = 1 + \
            max(D['B' if robot == 'O' else 'O'][0],
                abs(position - D[robot][1]) + D[robot][0])
        D[robot][1] = position
    print("Case #%d: %d" % (c+1, max(D["O"][0], D["B"][0])))
f.close()
