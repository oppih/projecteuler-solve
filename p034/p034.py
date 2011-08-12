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

zero2nineF = (1,1,2,jc(3),jc(4),jc(5),jc(6),jc(7),jc(8),jc(9))

@func_time
def sumFactorionPlus(uplimit):
    return sum(x for x in xrange(3, uplimit) if x == sum(zero2nineF[int(y)] for y in str(x)))

@func_time
def oneCrazyLine(uplimit):
    """
    http://projecteuler.net/index.php?section=forum&id=34
    """
    return sum(xxxx for xxxx in [int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])) for j in range(0, uplimit) if (j == int(reduce(lambda x, y: int(x) + int(y), [str(reduce(lambda x, y: x * y, range(1, int(i) + 1) + [1])) for i in str(j)])))])

# since:
# len(str(jc(9)*7)) = 7
# len(str(jc(9)*8)) = 7
# 8 digits would not result in an 8 digit number even with 99999999

if __name__ == "__main__":
    print sumFactorionPlus(7*jc(9)/60)
    print oneCrazyLine(7*jc(9)/60)
