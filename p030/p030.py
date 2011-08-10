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

"""
The highest 4-digit number is 9999.  9^5 + 9^5 + 9^5 + 9^5 = 236,196
5 digits, the highest sum of the 5th powers is 295,245
6 digits, the highest sum of the 5th powers is 354,294
7 digits, the highest sum of the 5th powers is 413,343
so, it's 6 digits!
"""
@func_time
def powerDigits(powers):
    return sum(x for x in xrange(2, powers) if sum(int(y)**5 for y in str(x)) == x)

if __name__ == "__main__":
    print powerDigits(200000)# since the numbers are:[4150, 4151, 54748, 92727, 93084, 194979]
