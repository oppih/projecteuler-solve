#!/usr/bin/env python

"""
this script is to test the speed of the two ways to calculate the gcd fo two random int.
"""
import random
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:\t\t", time.time()-start
    return _wrapper

random.seed("test")

def gcd_0(m, n):
    while n != 0:
        m, n = n, m % n
    return m

def gcd_1(a, b):
    return gcd_1(b, a%b) if b else a
    
@func_time     
def test_gcd_0():
    for i in xrange (100000):
        m = random.randint(1, 10000)
        n = random.randint(1, 10000)
        gcd_0(m, n)
    
@func_time
def test_gcd_1():
    for i in xrange (100000):
        m = random.randint(1, 10000)
        n = random.randint(1, 10000)
        gcd_1(m, n)
        
if __name__ == "__main__":
    test_gcd_0()
    test_gcd_1()
