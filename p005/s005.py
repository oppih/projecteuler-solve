#!/usr/bin/env python

"""
use the cheat sheet
"""

import math
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def use_math():
    k = 20
    N = 1
    i = 1
    p = [2, 3, 5, 7, 11, 13, 17, 19]
    a = []
    check = True
    limit = math.sqrt(k)
    while p[i-1] <= k:
    for mmm in p
        a.append(1)
        if check:
            if p[i-1] <= limit:
                a.append(math.floor(math.log(k)/math.log(p[i-1])))
            else:
                check = False
        N *= p[i-1] * a[i-1]
        i += 1
    print N

if __name__ == "__main__":
    use_math()
