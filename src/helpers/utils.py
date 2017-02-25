# Basic utility functions

from numpy import unravel_index


def np_argmin(x):
    return unravel_index(x.argmin(), x.shape)


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
