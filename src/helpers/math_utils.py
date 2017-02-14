# Mathematical Utility functions

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


def change_base(n, b):
    s = ""
    while n:
        s = str(n % b) + s
        n /= b
    return s


def is_happy_number(n, b):
    """
    find whether n (decimal) is a happy number in base b
    """
    visited = set([])
    while n > 1 and n not in visited:
        visited.add(n)
        s = 0
        while n:
            s += (n % b) ** 2
            n /= b
        n = s
    return n == 1, visited


def gcd_n(lst):
    return reduce(lambda x, y: gcd(x, y), lst)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
