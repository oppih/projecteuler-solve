#!/usr/bin/env python

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

http://projecteuler.net/index.php?section=problems&id=35
"""
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

def isPrime(num):
    if num == 0 or num == 1:
        return False
    for x in xrange(2, int(num**0.5)+1):
        if num % x == 0:
            return False
    else:
        return True

def isCircular(numstr):
    return isPrime(yy for yy in [int(numstr[i:] + numstr[:i]) for i in len(numstr)])

@func_time
def sumRotations(uplimit):
    return [x for x in xrange(2, uplimit) if isCircular(str(x))]

"""
Link below helped me understand what I need to get out:
    http://primes.utm.edu/glossary/page.php?sort=CircularPrime
"""

if __name__ == "__main__":
    print len(sumRotations(1000000))
