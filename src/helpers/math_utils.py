from scipy.special import comb as comb
import itertools
import math


def nCr(n, r):
    return comb(n, r)


def permutations(x):
    return list(itertools.permutations(x))


def prime_numbers(x):
    """ finds prime numbers till x (including x) using Sieve of Erathosthenes
        i^2 + ki <= x, k <= (x - i^2) / i
    """
    primes = set(range(2, x + 1))
    for i in range(2, int(math.sqrt(x))):
        if i in primes:
            for j in range(i**2, x+1, i):
                if j in primes:
                    primes.remove(j)
    return primes
