#!/usr/bin/env python

"""
use formula
see 006_overview.pdf for the algorithm.
"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def use_formula():
    limit = 100
    sum = limit * (limit + 1) / 2
    sum_sq = (2 * limit + 1) * (limit + 1) * limit / 6
    print sum ** 2 - sum_sq

if __name__ == "__main__":
    use_formula()
