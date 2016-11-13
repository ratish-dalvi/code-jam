"""
Skeleton to solve the problems
"""


def alg():
    pass

f = open("input.txt")
o = open("output.txt", "w")
T = int(f.readline().strip())
for i in range(T):
    n = f.readline().strip()

    # integer lists
    # v1 = map(int, f.readline().strip().split(" "))
    # v2 = map(int, f.readline().strip().split(" "))

    out = alg()
    o.write("Case #%d: %s\n" % (i+1, str(out)))

f.close()
o.close()
