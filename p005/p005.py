#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:\t\t", time.time()-start
    return _wrapper

@func_time
def manually_count():
    print "\nmanually way:"
    print 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

@func_time
def loop_way():
    """
    idea from stackoverflow
    http://stackoverflow.com/questions/2127039/smallest-number-that-is-evenly-divisible-by-all-of-the-numbers-from-1-to-20
    """
    

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def gcd_s(a, b):
    return gcd_s(b, a%b) if b else a # understand? from my test, it speeds up the function by TEN times.

@func_time
def gcd_reduce():
    print "\nuse gcd and reduce and lambda:"
    print reduce(lambda a, b: a*b/gcd(a,b), xrange(1, 20+1))

@func_time
def gcd_s_reduce():
    print "\nuse a short gcd with reduce and lambda:"
    print reduce(lambda a, b: a*b/gcd_s(a,b), xrange(1, 20+1))

if __name__ == "__main__":
    manually_count()
    gcd_reduce()
    gcd_s_reduce()

