#!/usr/bin/env python

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:\t\t", time.time()-start
    return _wrapper

@func_time
def manually_count():
    print "\nmanually way:"
    print 2**4 * 3**2 * 5 * 7 * 11 * 13 * 17 * 19

@func_time
def loop_way():
    """
    idea from stackoverflow
    http://stackoverflow.com/questions/2127039/smallest-number-that-is-evenly-divisible-by-all-of-the-numbers-from-1-to-20
    And, it took me 935.570346832 s to run it :(
    but I sped it up!!! finally.
    """
    addto = 2*3*5*7*11*13*17*19
    testNum, flag = addto, 0
    while flag == 0:
        #for i in xrange(2, 20+1):
        i = 2
        while i < 21:
            #print i, testNum
            if testNum % i != 0:
                break
            i += 1
        if i == 21:
            flag = 1
            print "\nthe loop way:"
            print testNum
        testNum += addto

def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def gcd_s(a, b):
    return gcd_s(b, a%b) if b else a
    # understand? from my test, it speeds up the function by TEN times.
    #from @yongsun : if b > 0: return gcd_s(b, a%b) else: return a
    # in C : return b? gcd(b, a%b): a

@func_time
def gcd_reduce():
    print "\nuse gcd and reduce and lambda:"
    print reduce(lambda a, b: a*b/gcd(a,b), xrange(1, 20+1))

@func_time
def gcd_s_reduce():
    print "\nuse a short gcd with reduce and lambda:"
    print reduce(lambda a, b: a*b/gcd_s(a,b), xrange(1, 20+1))

if __name__ == "__main__":
    manually_count()
    gcd_reduce()
    gcd_s_reduce()
    loop_way()
