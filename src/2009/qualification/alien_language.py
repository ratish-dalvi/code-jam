"""
https://code.google.com/codejam/contest/90101/dashboard#s=p0&a=0

It's better to go through every word and count instead of trying different
combinations and then checking if it is allowed as a word (cross referencing
with a dictionary).
So, for storing the pattern, we want something which has a set of allowed
letters for every index of the pattern. It is best (performance-wise) to use
a 2d Array of L X 26

(abc)(ef)abc -
   0  1  2  3  4  5  6  7 ... 25
   0  0  0  0  0  0  0  0 ...
0  1  1  1  0  0  0  0  0 ...        - abc
1  0  0  0  0  1  1  0  0 ...        - ef
2  1  0  0  0  0  0  0  0            - a
3  0  1  0  0  0  0  0  0            - b
.  0  0  1  0  0  0  0  0            - c
.
L-1

Large dataset finishes in 5 seconds
"""
import sys
import numpy as np

f = open(sys.argv[1])

# alphabet, words, test cases
L, D, N = map(int, f.readline().strip().split(" "))
words = [f.readline().strip() for i in range(D)]
for c in range(N):
    arr = np.zeros((L, 26))
    inp = f.readline().strip()
    i = j = 0
    while j < len(inp):
        if inp[j] == "(":
            j += 1
            while inp[j] != ")":
                arr[i][ord(inp[j]) - ord('a')] = True
                j += 1
        else:
            arr[i][ord(inp[j]) - ord('a')] = True
        i += 1
        j += 1
    cnt = 0
    for word in words:
        present = 1
        for i in range(len(word)):
            if not arr[i][ord(word[i]) - ord('a')]:
                present = 0
                break
        cnt += present
    print("Case #%d: %d" % (c+1, cnt))

f.close()
