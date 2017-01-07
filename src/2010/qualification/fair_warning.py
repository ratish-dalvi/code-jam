"""
Skeleton to solve the problems
"""
import os
import sys
sys.path.append(os.path.abspath('./src/helpers'))
from math_utils import gcd_n

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    numbers = map(int, f.readline().strip().split(" "))[1:]
    g = gcd_n(
        [abs(numbers[i-1] - numbers[i]) for i in range(1, len(numbers))])
    print("Case #%d: %d" % (c+1, (g - numbers[0] % g) % g))
f.close()
