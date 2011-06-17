#!/usr/bin/env python

"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt, floor
import time
def func_time(func):
    """
    New decorator from @yongsun
    """
    def _wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
        return ret

    _wrapper.__name__ = func.__name__
    return _wrapper

def isprime(n):
    """
    from s007.py
    """
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        flag = True
        while f <= r:
            if n % f == 0:
                flag = False
                break
            if n % (f+2) == 0:
                flag = False
                break
            f += 6
        return flag

@func_time
def findPrimeSum():
    sumPrime = 0
    for x in xrange(2, 2000000):
        if isprime(x):
            sumPrime += x
        else:
            pass
    return sumPrime

@func_time
def betterPrimeSum():
    limit = 2000000
    sumPrime = 2 + 3
    n = 5
    while n < limit:
        if isprime(n):
            sumPrime += n
        n += 2
        if n < limit and isprime(n):
            sumPrime += n
        n += 4
    return sumPrime
    
if __name__ == "__main__":
    print findPrimeSum()
    print betterPrimeSum()
