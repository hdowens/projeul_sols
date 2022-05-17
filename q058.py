from timeit import default_timer
from fractions import Fraction
from math import sqrt
import random

#NOT MY CODE, SOMEONE ELSE'S
"""
def is_prime(n):
    #Miller-Rabin test
    if n!=int(n):
        return False
    n=int(n)
    if n==0 or n==1 or n==4 or n==6 or n==8 or n==9:
        return False
 
    if n==2 or n==3 or n==5 or n==7:
        return True
    s = 0
    d = n-1
    while d%2==0:
        d>>=1
        s+=1
    assert(2**s * d == n-1)
 
    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True  
 
    for i in range(8):#number of trials 
        a = random.randrange(2, n)
        if trial_composite(a):
            return False
 
    return True  
"""

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def compute():
    #in the 5 by 5 spiral we know that the top right hand side
    #number is the last, so that is the limit to our loop
    limit = 100_000_000_000

    #lsum is the var keeping track of the sum
    #step is at 2 which is the current jump between numbers to be added to the sum (3,5,7,9)
    #but every 4 numbers the jump increases by 2, e.g. (13,7,21,25) are the next ones.
    #so when count is a multiple of 4, step will increase by 2. Just before this, we know
    #that the spiral will have done a full loop, so we need to check diagonals.
    prime_count = 0
    step, count, iter = 2, 0, 3
    while iter <= limit:
        count += 1
        if count % 4 == 0:
            if Fraction(prime_count, (2*step) + 1) < Fraction(1,10):
                break
            step += 2
        if is_prime(iter):
            prime_count += 1      
        iter += step
    return step+1


if __name__ == "__main__":
      
    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
