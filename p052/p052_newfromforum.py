from func_time import func_time
"""
from http://projecteuler.net/thread=52;page=2
"""

def digitsToStr(digit):
    return set(str(digit))

@func_time
def newSolve():
    n = 2
    while True:
        if digitsToStr(n) == digitsToStr(2*n) == digitsToStr(3*n) == digitsToStr(4*n) == digitsToStr(5*n) == digitsToStr(6*n):
            return n
        else:
            n += 1
    
if __name__ == "__main__":
    print newSolve()
