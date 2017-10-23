# Basic utility functions

from numpy import unravel_index
import math


def np_argmin(X, lean=True):
    if lean:
        return unravel_index(X.argmin(), X.shape)
    else:
        idx = unravel_index(X.argmin(), X.shape)
        return idx, X[idx]


def maximum_contiguous_subarray(lst):
    """ computes the maximum contiguous subarray in the given array using
    Kadane's algorithm
    """
    current_sprint = 0
    max_so_far = 0
    for x in lst:
        current_sprint = max(current_sprint + x, 0)
        max_so_far = max(current_sprint, max_so_far)
    return max_so_far


def get_path_from_root(x):
    """ given x, get its path on a binary tree"""
    l = math.floor(math.log(x, 2))  # level, starting from 0
    y = x - (2**l - 1)  # number of elements at level l
    lst = []
    while l > 0:
        lst.append("L" if y % 2 else "R")
        y = math.ceil(y/2)
        l -= 1
    return list(reversed(lst))
