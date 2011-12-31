from func_time import func_time
"""
from http://www.s-anand.net/euler.html # 52
much faster
"""

def multiples_have_same_digits(n):
    digit_keys = dict.fromkeys(list(str(n)))
    for x in xrange(2, 4):
        for d in list(str(x * n)):
            if not digit_keys.has_key(d): return False
    return True

@func_time
def newSolve():
    n = 0 + 9
    while True:
        if multiples_have_same_digits(n):
            return n
        else:
            n = n + 9  # n must be a multiple of 9 for this to happen

if __name__ == "__main__":
    print newSolve()
