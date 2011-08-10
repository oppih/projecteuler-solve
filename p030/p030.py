#!/usr/bin/env python

"""
http://projecteuler.net/index.php?section=problems&id=30
"""
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
def powerDigits(topNum):
    return sum(x for x in xrange(2, topNum) if sum(int(y)**5 for y in str(x)) == x)

if __name__ == "__main__":
    print powerDigits(200000)
