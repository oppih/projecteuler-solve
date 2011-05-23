#!/usr/bin/env python

"""
This script is used to count rumtime.

It's strange that I used a virable to store the result of a*b but it takes more time.
"""

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
def solve004_0():
    biggest_0 = 0
    a = 999
    while a >= 100:
        if a % 11 == 0:
            b, db = 999, 1
        else:
            b, db = 990, 11 # the biggest number less than or equal 999 and divisible by 11
        while b >= a:
            if a * b <= biggest_0:
                break # why 'break' ?
            if is_palindrome(a * b):
                biggest_0 = a * b
            b -= db
        a -= 1
    print biggest_0

@func_time
def solve004_1():
    biggest_1 = 0
    a = 999
    while a >= 100:
        if a % 11 == 0:
            b, db = 999, 1
        else:
            b, db = 990, 11 # the biggest number less than or equal 999 and divisible by 11
        while b >= a:
            if a * b <= biggest_1:
                break # why 'break' ?
            if is_palindrome(a * b):
                biggest_1 = a * b
            b -= db
        a -= 1
    print biggest_1

if __name__ == "__main__":
    print "I use two functions to compare time:"
    solve004_0()
    solve004_1()
