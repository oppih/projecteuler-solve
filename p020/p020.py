#!/usr/bin/env python

"""
This script is used to count rumtime.
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
def sumOfN(startNum):
    return sum(int(x) for x in str(reduce(lambda x,y:x*y, xrange(1, startNum+1))))

if __name__ == "__main__":
    print sumOfN(100)
