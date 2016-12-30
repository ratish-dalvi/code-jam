"""
https://code.google.com/codejam/contest/186264/dashboard#s=p1
"""
import sys

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    num = list(f.readline().strip())
    if sorted(num, reverse=True) == num:
        num.insert(0, '0')
    for i in reversed(range(len(num)-1)):
        if num[i] < num[i+1]:
            break
    for j in range(len(num)-1, i, -1):
        if num[j] > num[i]:
            break
    out = "".join(num[:i] + [num[j]] + sorted(num[i:j] + num[j+1:]))
    print("Case #%d: %s" % (c+1, str(out)))

f.close()
