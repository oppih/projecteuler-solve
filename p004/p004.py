#!/usr/bin/env python

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# got the solution mainly from StackOverFlow:
# http://stackoverflow.com/questions/555009/euler-problem-number-4

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

def is_palindrome(n):
    s = str(n)
    return s == s[::-1] # reverse a string totally

@func_time
def biggest():
    big_x, big_y, max_seen = 0, 0, 0
    for x in xrange(999, 99, -1):
        for y in xrange(x, 99, -1): # so we don't double count
            xy = x * y
            if xy < max_seen: continue # since we're decrease dounting, there's nothing bigger than the first max_seen number.
            if is_palindrome(xy):
                big_x, big_y, max_seen = x, y, xy
    print big_x, big_y, max_seen

# xrange is Like range(), but instead of returning a list, returns an object that generates the numbers in the range on demand.  For looping, this is slightly faster than range() and more memory efficient.

if __name__ == "__main__":
    biggest()
