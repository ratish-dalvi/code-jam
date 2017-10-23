"""
https://code.google.com/codejam/contest/1460488/dashboard
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

inp = [
    "ejp mysljylc kd kxveddknmc re jsicpdrysi",
    "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
    "de kr kd eoya kw aej tysr re ujdr lkgc jv",
    "y qee",
]
out = [
    "our language is impossible to understand",
    "there are twenty six factorial possibilities",
    "so it is okay if you want to just give up",
    "a zoo"
]


mapping = {chr(x + ord('a')): None for x in range(26)}
mapping[' '] = ' '

for i in range(len(inp)):
    for j in range(len(inp[i])):
        letter = inp[i][j]
        if mapping[letter] is not None:
            assert mapping[letter] == out[i][j]
        else:
            mapping[letter] = out[i][j]

assert set(mapping.values()) - set(mapping.keys()) == set([None])
# set(mapping.keys()) - set(mapping.values())] = q  #  Get the remainder
mapping['z'] = 'q'


T = int(f.readline().strip())
for c in range(T):
    out = map(lambda x: mapping[x], f.readline().strip())
    print("Case #%d: %s" % (c+1, "".join(out)))

f.close()
