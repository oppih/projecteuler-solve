#!/usr/bin/env python

"""
Problem:http://projecteuler.net/index.php?section=problems&id=34
About Factorion:http://mathworld.wolfram.com/Factorion.html
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

def jc(n):
    return reduce(lambda x,y:x*y, xrange(1, n+1))

zero2nine = (1,1,2,jc(3),jc(4),jc(5),jc(6),jc(7),jc(8),jc(9))

def isFactorion(nn):
    sumxx = 0
    for x in str(nn):
        sumxx += zero2nine[int(x)]
    if nn == sumxx:
        return True
    else:
        return False

@func_time
def sumFactorion(uplimit):
    return sum(x for x in xrange(3, uplimit) if isFactorion(x))

if __name__ == "__main__":
    print sumFactorion(7*jc(9))
