"""
You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The scalar
 product of these vectors is a single number, calculated as x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as you wish.
Choose two permutations such that the scalar product of your two new vectors
is the smallest possible, and output that minimum scalar product.
"""
import numpy as np

f = open("input.in")
o = open("output.txt", "w")

T = int(f.readline().strip())
for i in range(T):
    n = f.readline().strip()
    v1 = map(int, f.readline().strip().split(" "))
    v2 = map(int, f.readline().strip().split(" "))
    out = np.dot(sorted(v1), sorted(v2, reverse=True))
    o.write("Case #%d: %s\n" % (i+1, str(out)))

f.close()
o.close()
