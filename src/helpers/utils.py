from numpy import unravel_index


def np_argmin(x):
    return unravel_index(x.argmin(), x.shape)
