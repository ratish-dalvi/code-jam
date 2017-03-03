"""
https://code.google.com/codejam/contest/975485/dashboard#s=p1
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    lst = f.readline().strip().split(" ")
    ii = 0
    # Read 'combine'
    base = set(["Q", "W", "E", "R", "A", "S", "D", "F"])
    d_comb = {}
    for i in range(int(lst[ii])):
        ii += 1
        d_comb[lst[ii][0] + lst[ii][1]] = lst[ii][2]
        d_comb[lst[ii][1] + lst[ii][0]] = lst[ii][2]

    # Read 'oppose'
    d_opp = {k: [] for k in list(base)}
    ii += 1
    for i in range(int(lst[ii])):
        ii += 1
        d_opp[lst[ii][0]].append(lst[ii][1])
        d_opp[lst[ii][1]].append(lst[ii][0])

    # Read all characters
    d_letters = {}
    letters = list(lst[ii+2])

    prev = []
    for i in range(len(letters)):
        x = letters[i]
        if x not in base:
            prev.append(x)
            continue
        else:
            if len(prev) == 0:
                prev.append(x)
                d_letters[x] = 1
                continue

        last_two = "".join(x + prev[-1])
        if last_two in d_comb:
            if prev[-1] in d_letters:
                d_letters[prev[-1]] -= 1
            prev = prev[:-1] + [d_comb[last_two]]
        elif any(True for y in d_opp[x] if d_letters.get(y, 0) > 0):
            prev = []
            d_letters = {}
        else:
            prev.append(x)
            d_letters[x] = d_letters.get(x, 0) + 1

    print("Case #%d: [%s]" % (c+1, ", ".join(prev)))

f.close()
