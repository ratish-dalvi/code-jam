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
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


def alg():
    return

T = int(f.readline().strip())
for i in range(T):
    n = f.readline().strip()

    # TODO

    out = alg()
    print("Case #%d: %s\n" % (i+1, str(out)))

f.close()
