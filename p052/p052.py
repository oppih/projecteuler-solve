#!/usr/bin/env python

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

from func_time import func_time

@func_time
def findSameDigit():
    isFound = False
    for i in xrange(2, 1000000):
        for j in xrange(2, 7):
            if set(str(i)) == set(str(i*j)) and j == 6:
                isFound = True
                break
            elif set(str(i)) == set(str(i*j)):
                continue
            else:
                break
        if isFound == True:
            return i

if __name__ == "__main__":
    print findSameDigit()

