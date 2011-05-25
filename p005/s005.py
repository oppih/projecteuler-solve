#!/usr/bin/env python

"""
use the cheat sheet
maybe this feature needs some list tricks?
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
    #i = 1
    p = [2, 3, 5, 7, 11, 13, 17, 19]
    a = []
    check = True
    limit = math.sqrt(k)
    # while p[i-1] <= k:
    for mmm in p:
        a.append(1)
        if mmm <= k:
            if check:
                if mmm <= limit:
                    print mmm, a
                    a.append(int(math.floor(math.log(k)/math.log(mmm))))
                    print a
                    print
                else:
                    check = False
        nnn = a.pop()
        print nnn
        N *= mmm * nnn
        b = []
        b.append(nnn)
        a = b + a
        print a
            #i += 1
    print N * 3

if __name__ == "__main__":
    use_math()
