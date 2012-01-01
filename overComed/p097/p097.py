#!/usr/bin/env python

"""
Find the last ten digits of this prime number:28433*2^7830457+1
"""

from func_time import func_time

@func_time
def getLastOfPrime():
    return str(28433 * pow(2, 7830457) + 1)[-10:]

@func_time
def newWayInPython():
    return str(((28433*pow(2, 7830457))+1) % 10000000000)[-10:]

if __name__ == "__main__":
    #print getLastOfPrime()
    print newWayInPython()

