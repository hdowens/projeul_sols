from timeit import default_timer
from fractions import Fraction
from math import log10
import sys



"""
ATTEMPT 1 - FRACTIONS & RECURSION


def sqrt_recur(lim):
    if lim == 1: return Fraction(1,2)
    else:
        return Fraction(1, 2 + sqrt_recur(lim - 1))


def compute():
    sum = 0
    for i in range(1, 1001):
        numer,denom =  (1 + sqrt_recur(i)).numerator, (1 + sqrt_recur(i)).denominator
        if  int(log10(numer)) >int(log10(denom)):
            sum += 1
 
    return sum
"""
def compute_att2():
    count = 0
    numer, denom = 3, 2
    for i in range(1001):
        numer, denom = numer + 2 * denom, numer + denom
        count += int(log10(numer)) >int(log10(denom))
    return count

if __name__ == "__main__":
      
    start = default_timer()

    print(compute_att2())

    stop = default_timer()

    print("Time taken -> ", stop - start)
