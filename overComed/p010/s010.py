#!/usr/bin/env python

"""
This script is used to count rumtime.
"""
from math import sqrt
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

@func_time
def sieveWay():
    limit = 2000000
    sievebound = int((limit - 1)/2) # last index of sieve
    sieve = [False] * sievebound
    crosslimit = int((sqrt(limit) - 1)/2)
    for i in xrange(1, crosslimit+1):
        if not sieve[i]:# 2*i+1 is prime, mark multiples
            for j in xrange(2 * i * (i+1), sievebound, 2*i+1):
                sieve[j] = True
    sumPrime = 2
    #print sieve[:10]
    for i in xrange(1, sievebound):#if not start with 1, 2*0+1=1 will be added
        if not sieve[i]:# only False position will be added
            sumPrime += (2*i+1)
    return sumPrime

if __name__ == "__main__":
    print sieveWay()
