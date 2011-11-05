#!/usr/bin/env python

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
    while n > 0:
        digits.append(str(n % base))
        n = n / base
    return digits == digits[::-1]

def makePalindrome(n, base, oddlength):
    "To try a new palindrome generator"
    "And this is a demo, we will not use this function below."
    res = n
    if oddlength:
        n /= base
    while n > 0:
        res = base*res + n % base
        n /= base
    return res

def makePalindromeBase2(n, oddlength): # oddlength for 'xyzzyx' or 'xyzyx'
    "To generate palindromes in base 2 this function can be made more efficient using"
    "'shift' and 'and' operations rather than 'mod' and 'div' operators like this"
    res = n
    if oddlength:
        n = n >> 1
    while n > 0:
        res = res << 1 + n and 1
        n = n >> 1
    return res

@func_time
def sumPalindrome():
    limit = 1000000
    sumPalind = 0
    
    i = 1
    p = makePalindromeBase2(i, True)
    while p < limit:
        if isPalindrome(p, 10):
            sumPalind += p
        i += 1
        p = makePalindromeBase2(i, True)
        
    i = 1
    p = makePalindromeBase2(i, False)
    while p < limit:
        if isPalindrome(p, 10):
            sumPalind += p
        i += 1
        p = makePalindromeBase2(i, False)
    
    return sumPalind

if __name__ == "__main__":
    print sumPalindrome()
