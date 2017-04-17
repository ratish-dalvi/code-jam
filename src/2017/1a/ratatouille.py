"""
https://code.google.com/codejam/contest/5304486/dashboard#s=p1
"""
import os
import sys
import numpy as np
import math
sys.path.append(os.path.abspath('./src/helpers'))

f = open(sys.argv[1])

T = int(f.readline().strip())
for c in range(T):
    N, P = map(int, f.readline().strip().split(" "))
    serving_sizes = map(int, f.readline().strip().split(" "))
    # Sorting the packet sizes makes it easily solvable
    arr = np.array(
        [sorted(map(float, f.readline().strip().split(" ")))
         for i in range(N)])
    arr_out = np.array([[None for i in range(P)] for j in range(N)])
    for i in range(N):
        for j in range(P):
            ss = serving_sizes[i]
            k = int(math.ceil(arr[i, j]/ss))
            lst = []
            while ss*k*0.9 <= arr[i, j] and arr[i, j] <= ss*k*1.1:
                lst.append(k)
                k -= 1
            k = int(math.floor(arr[i, j]/ss))
            while ss*k*0.9 <= arr[i, j] and arr[i, j] <= ss*k*1.1:
                lst.append(k)
                k += 1
            arr_out[i, j] = set(lst)
    cnt = 0
    inds = [0]*N
    for i in range(P):
        s = arr_out[0][i]
        for j in range(N):
            packet_found = False
            for k in range(inds[j], P):
                if s & arr_out[j][k]:
                    s = s & arr_out[j][k]
                    inds[j] = k+1
                    packet_found = True
                    break
            if not packet_found:
                break
        if not packet_found:
            continue
        cnt += 1
    print("Case #%d: %s" % (c+1, cnt))

f.close()
