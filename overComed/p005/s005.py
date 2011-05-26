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
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def use_math():
    k, N = 20, 1
    p = [2, 3, 5, 7, 11, 13, 17, 19]
    a = [1]*8
    check = True
    limit = math.sqrt(k)
    for i in xrange(8):
        if check:
            if p[i] <= limit:
                a[i] = int(math.floor(math.log(k)/math.log(p[i])))
                #print str(p[i]) + "^" + str(a[i])
            else:
                check = False
        N *= p[i] ** a[i] # I was using * not ** ! foolish mistake!
    print N

if __name__ == "__main__":
    use_math()
