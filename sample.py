#!/usr/bin/env python

"""
DESCRIPTION
"""

import time
def func_time(func):
    def _wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print func.__name__, "run:", time.time()-start
    return _wrapper

@func_time
