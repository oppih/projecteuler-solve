#!/usr/bin/env python

"""
idea from solution
"""

limit = 4000000
sum002 = 0
a = 1
b = 1
while b < limit:
    if b % 2 == 0:
        sum002 += b
    h = a + b
    a = b
    b = h

print sum002
