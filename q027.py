import timeit
import itertools
import math

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_sieve(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes


def get_answer():
    maxa, maxb, maxs = 0,0,0
    p = primes_sieve(1000)
    for i in range(-1000,1000):
        for j in p:
            n = 0
            while(is_prime(abs(n*n + i*n + j))):
                n += 1
            if n > maxs:
                maxa,maxb,maxs = i,j,n

    return maxa * maxb

    
if __name__ == '__main__':
    start = timeit.default_timer()
    
    
    print(get_answer())

    stop = timeit.default_timer()

    print("Time taken -> ",stop-start)
