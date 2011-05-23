#!/usr/bin/env python

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

import time
def func_time(func):
	def _wrapper(*args, **kwargs):
		start = time.time()
		func(*args, **kwargs)
		print func.__name__, "run:", time.time()-start
	return _wrapper

@func_time
def p001():
	sump001 = 0
	for i in range(3,1000):
		if i % 3 == 0 or i % 5 == 0:
			sump001 += i
	print sump001

if __name__ == "__main__":
	p001()