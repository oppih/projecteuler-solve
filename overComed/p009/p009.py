#!/usr/bin/env python

"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def triplet():
    s = 1000
    for a in xrange(3, int((s-3)/3)+1):
        for b in xrange(a+1, (s-1-a)/2):
            c = s - a - b
            if a**2 + b**2 == c**2:
                print a, b, c, a*b*c

if __name__ == "__main__":
    triplet()

