#!/usr/bin/env python

"""
This script is used to count rumtime.
"""
from math import *
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

@func_time
def useAlgorithm():
    s1 = 1000
    s2 = s1 / 2
    mlimit = int(sqrt(s2)) - 1

    for m in xrange(2, mlimit + 1):
        if s2 % m == 0:
            sm = s2 / m
            while sm % 2 == 0:
                sm /= 2

            if m % 2 == 1:
                k = m + 2
            else:
                k = m + 1

            while k < 2*m and k <= sm:
                if sm % k == 0 and gcd(k, m) == 1:
                    d = s2 / (k * m)
                    n = k - m
                    a = d * (m**2 - n**2)
                    b = 2 * d * m * n
                    c = d * (m**2 + n**2)
                    print a, b, c, a*b*c
                k += 2

if __name__ == "__main__":
    useAlgorithm()
