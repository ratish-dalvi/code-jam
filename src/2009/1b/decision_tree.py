"""
Skeleton to solve the problems
https://code.google.com/codejam/contest/186264/dashboard#s=p0&a=0
"""
import os
import regex
import sys
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])


def go(tree, features):
    if isinstance(tree, tuple):
        if len(tree) > 1:
            return tree[0] * go(tree[2], features) if tree[1] in features \
                else tree[0] * go(tree[3], features)
    else:
        return tree

T = int(f.readline().strip())
for c in range(T):
    tree = " ".join(
        [f.readline().strip() for i in range(int(f.readline().strip()))])
    tree = regex.sub(r"\(\s*", "(", tree)
    tree = regex.sub(r"\s*\)", ")", tree)
    tree = regex.sub(r"\s+", ",", tree)
    tree = regex.sub(r",(?=[a-z])", ",'", tree)
    tree = eval(regex.sub(r"(?<=[a-z]),", "',", tree))
    print("Case #%d:" % (c+1))
    for i in range(int(f.readline().strip())):
        feats = set(f.readline().strip().split(" ")[2:])
        print("%.8f" % go(tree, feats))

f.close()
