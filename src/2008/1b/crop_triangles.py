"""
Link: https://code.google.com/codejam/contest/32017/dashboard#s=p0&a=0

(a + b + c) / 3 = N  where N is an integer
Let a = 3*a_1 + ar, b = 3*b1 + br ... where ar, br, cr belong to {0, 1, 2}

So, we'll get:
N1 + (ar + br + cr) / 3 = N  ...  where N, N1 are integers
So (ar + b3 + c3) should be a multipl of 3- either 0, 3 or 6
only 3 ways are possible
        ar  br  cr
    0 | 0   0   0
    3 | 0   1   2   - all combinations
    3 | 1   1   1
    6 | 2   2   2

So, they should either be all same or all different.

Combined, X and Y will fall into 9 groups

   X\Y |  0    1    2
  -------------------
    0  |  00   01  02
    1  |  10   11  12
    2  |  20   21  22

We need to choose 3 points such that the follwing cases are satisfied
S - all the values are same
D - all the values are different

  X  Y  |  How
  ----------------
  S  S  | all 3 from the same cell.        sum_i sum_j (x_i y_j choose 3)
  S  D  | each from same row diff column.  sum_i mul_j xi * yj
  D  S  | each from same column diff row   sum_j mul_i xi * yj
  D  D  | each from diff col diff row
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))
import utils
from utils import nCr, permutations
f = open(sys.argv[1])


def perm(x):
    for y in x:
        return perm(x)

T = int(f.readline().strip())
for i in range(T):
    n, A, B, C, D, x0, y0, M = map(int, f.readline().split(" "))
    arr = [[0, 0, 0] for j in range(3)]  # Initialize 3 * 3 array

    # generate and store data
    X = x0
    Y = y0
    arr[X % 3][Y % 3] += 1
    for j in range(n-1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        arr[X % 3][Y % 3] += 1

    perm_012 = permutations([0, 1, 2])
    r = 0
    r += reduce(lambda x, y: x + nCr(y, 3), [x for y in arr for x in y], 0)
    r += reduce(lambda x, y: x + np.prod(y), arr, 0)  # SD
    r += sum([reduce(lambda x, y: x * y[j], arr, 0) for j in range(3)])  # DS
    r += sum([arr[0][pp[0]] * arr[1][pp[1]] * arr[2][pp[2]]
              for pp in perm_012])  # DD
    print("Case #%d: %s" % (i+1, str(int(r))))

f.close()
