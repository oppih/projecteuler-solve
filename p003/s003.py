#!/usr/bin/env python

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
from math import sqrt
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def find_biggest_factor():
    n = 600851475143
    if n % 2 == 0:
        lastFactor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2
    else:
        lastFactor = 1

    factor = 3

    maxFactor = sqrt(n)

    while n > 1 and factor < maxFactor:
        if n % factor == 0:
            n /= factor
            lastFactor = factor
            while n % factor == 0:
                n /= factor
            maxFactor = sqrt(n)
        factor += 2

    if n == 1:
        print lastFactor
    else:
        print n

if __name__ == "__main__":
    find_biggest_factor()