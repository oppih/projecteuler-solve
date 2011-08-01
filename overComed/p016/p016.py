#!/usr/bin/env python

"""
http://projecteuler.net/index.php?section=problems&id=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
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
def xxTimes(times):
    resultStr = str(2**times)
    summ = 0
    for i in xrange(len(resultStr)):
        summ += int(resultStr[i])
    return summ

@func_time
def onelineSolver(times):
    return sum(int(i) for i in str(pow(2, times)))

if __name__ == "__main__":
    print xxTimes(1000)
    print onelineSolver(1000)

