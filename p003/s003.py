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

n = 600851475143

@func_time
def find_biggest_factor():
    if n % 2 == 0:
        """
        deal with n is even number
        """
        lastFactor = 2
        n /= 2
        while n % 2 == 0:
            n /= 2
    else:
        # n is odd number
        lastFactor = 1

    factor = 3 # start from a proper number:3

    maxFactor = sqrt(n) # save time

    while n > 1 and factor < maxFactor:
        if n % factor == 0:
            n /= factor
            lastFactor = factor
            while n % factor == 0:
                n /= factor
                # calculate untill n cannot be dived by lasfFactor
            maxFactor = sqrt(n)
            # stat a new circle to calculate the factor
        factor += 2
        # jump to next odd number (it may be a factor)

    if n == 1:
        print lastFactor
        # if n equals lastFator
    else:
        print n
        # if n cannot be divided anymore

if __name__ == "__main__":
    find_biggest_factor()
