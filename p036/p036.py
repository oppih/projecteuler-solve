#!/usr/bin/env python

"""
http://projecteuler.net/index.php?section=problems&id=36

The decimal number, 585 = (1001001001)2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
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

def isPalindrome(n, base):
    digits = []
    reverses = []
    while n > 0:
        d = str(n % base)
        digits.append(d)
        reverses.insert(0, d)
        n = n / base
    #return digits == digits[::-1]
    return digits == reverses

@func_time
def sumPalindrome():
    return sum(n for n in xrange(1, 1000000) if isPalindrome(n, 10) and isPalindrome(n, 2))

if __name__ == "__main__":
    print sumPalindrome()
