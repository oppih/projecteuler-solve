#!/usr/bin/env python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?


This problem is easy and the cheat sheel use the similiar way with mine,
"""

from math import *
import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

# prime numbers are only divisible by unity and themselves
# (1 is not considered a prime number by convention)

def isprime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = floor(sqrt(n))
        f = 5
        flag = True
        while f <= r:
            if n % f == 0:
                flag = False
                break
            if n % (f+2) == 0:
                flag = False
                break
            f += 6
        return flag

@func_time
def find_prime():
    count = 1
    prime_s = 3
    while count < 10001:
        if isprime(prime_s):
            count += 1
        prime_s += 2
    print prime_s - 2

if __name__ == "__main__":
    print "The 10001th prime number is: "
    find_prime()
