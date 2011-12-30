#!/usr/bin/env python

#  Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

from func_time import func_time

@func_time
def getLastTenDigits(topNumber):
    return str(sum(pow(x, x) for x in xrange(1, topNumber+1)))[-10:]

if __name__ == "__main__":
    print getLastTenDigits(1000)
