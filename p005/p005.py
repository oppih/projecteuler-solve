#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run:", time.time()-start
    return _wrapper

@func_time

def gcd(m, n):
    while not n == 0:
        m, n = n, m % n
    return m * n / m