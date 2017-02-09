"""
https://code.google.com/codejam/contest/1145485/dashboard#s=p0&a=0
Complexity O(mn)

Running time - Large program runs in ~70 seconds
the words are stored as:
eg. aa baaz
         characters
Words |  a        b      .  .      z
--------------------------------------
1       (0, 1)
.       (1, 2)   (0)              (3)
.
N
"""
import os
import sys
import numpy as np
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

aa = ord("a")  # 97


def go(alphabet, arr, remaining, dist):
    if dist == 0:
        return (0, remaining[0])  # loss, word_pos

    for k in range(len(alphabet)):
        x = ord(alphabet[k]) - aa
        d = {}  # [letter_pos, letter_pos2]: [word_pos1, word_pos2]
        for i in remaining:
            y = arr[i][x]
            if y not in d:
                d[y] = [i]
            else:
                d[y].append(i)
        # Continue if letter is not consistent with any of the remaining words
        if not(len(d) == 1 and () in d):
            break

    max_loss = -np.inf
    for tup, word_inds in d.iteritems():
        loss, w_pos = go(alphabet[k+1:], arr, word_inds, dist-len(tup))
        loss += (len(tup) == 0)
        if max_loss < loss:
            best_word = w_pos
            max_loss = loss
        elif max_loss == loss:
            best_word = min(best_word, w_pos)

    return (max_loss, best_word)


T = int(f.readline().strip())
for c in range(T):
    N, M = map(int, f.readline().strip().split(" "))
    words = [f.readline().strip() for i in range(N)]
    lst_alphabets = [f.readline().strip() for i in range(M)]

    # Pre-process words:
    #   Form sets of words with the same length
    #   Store the words in an array-format mentioned above
    len_sets = {i: [] for i in range(1, 11)}
    arr = []
    for k, word in enumerate(words):
        tmp = [() for i in range(26)]
        for i, y in enumerate(word):  # each char
            tmp[ord(y) - aa] += (i,)
        arr.append(tmp)
        len_sets[len(word)].append(k)  # length-based sets
    arr = np.array(arr)  # using numpy for large arrays

    # Now run the algorithm for each list of alphabets
    out = []
    for alphabet in lst_alphabets:
        best_loss = ibest_word = 0
        for length, word_set in len_sets.iteritems():
            if len(word_set) == 0:
                continue
            loss, iword = go(alphabet, arr, word_set, length)
            if best_loss < loss:
                best_loss = loss
                ibest_word = iword
            elif best_loss == loss:
                ibest_word = min(ibest_word, iword)
        out.append(words[ibest_word])
    print("Case #%d: %s" % (c+1, " ".join(out)))

f.close()
