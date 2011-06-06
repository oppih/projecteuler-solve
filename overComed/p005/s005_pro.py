#!/usr/bin/env python

"""
use the cheat sheet
maybe this feature needs some list tricks?

After working on it for about three hours, I got it.
It should be quick enought.
"""

import math
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
        return ret

    _wrapper.__name__ = func.__name__
    return _wrapper

@func_time
def use_math():
    k, N = 20, 1
    primes = (2, 3, 5, 7, 11, 13, 17, 19)

    limit = math.sqrt(k)

    for p in primes:
        fac = int(math.log(k)/math.log(p)) if p <= limit else 1
        N *= p ** fac;

    return N

if __name__ == "__main__":
    print use_math()
