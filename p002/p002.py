#!/usr/bin/env python

"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""
from math import sqrt
import time

def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run time:", time.time()-start
    return _wrapper

@func_time
def Fib(n):
    print ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))

'''
def fib(n):
	"""
	This part contains problem: NoneType `fib` cannot use '+'
	"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
'''

# fib(34) = 5702887 > 4000000
# fib(33) = 3524578 < 4000000

#x = int(raw_input("Input a number?\n>"))
x = 33
if __name__ == "__main__":
	Fib(x)
	
