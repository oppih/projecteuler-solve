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
    """
    I'll try to shorten this part.
    """
    sumxx = 0
    for x in str(nn):
        sumxx += zero2nine[int(x)]
    if nn == sumxx:
        return True
    else:
        return False

def isFactorionPlus(nn):
    return nn == sum(zero2nine[int(x)] for x in str(nn))

@func_time
def sumFactorion(uplimit):
    return sum(x for x in xrange(3, uplimit) if isFactorionPlus(x))

@func_time
def sumFactorionPlus(uplimit):
    return sum(x for x in xrange(3, uplimit) if x ==sum(zero2nine[int(y)] for y in str(x)))

# since:
# len(str(jc(9)*7)) = 7
# len(str(jc(9)*8)) = 7
# 8 digits would not result in an 8 digit number even with 99999999

if __name__ == "__main__":
    print sumFactorion(7*jc(9))
    print sumFactorionPlus(7*jc(9))
