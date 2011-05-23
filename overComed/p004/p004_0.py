#!/usr/bin/env python

"""
This solution is from http://www.agapow.net/programming/python/euler/004 , but it seem the result they give out is wrong?

Besides, I tested the code, but it's strange that it's a small number. I cannot understand it.

Need more development.

I've figured out what's wrong with this function.
It's only use n ** 2, not every posible two numbers.
So I decided to give up it here.

More time should be focused on the way in 004_over_view.pdf used.
"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def string_way():
    max = None
    for i in xrange(9, 0, -1):
        for j in xrange(9, -1, -1):
            for k in xrange(9, 0, -1):
                n = (i * 100) + (j * 10) + k
                s = str(n ** 2) # it's wrong here because it only produce n * n, the number itself.
                midpt = len(s) / 2
                if s[:midpt] == s[-midpt:][::-1]:
                    max = s
    print n, max

if __name__ == "__main__":
    string_way()
