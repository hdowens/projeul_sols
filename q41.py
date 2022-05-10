from timeit import default_timer
from math import sqrt

def pandigital(number, digit):
    return {f'{i}' for i in range(1,digit+1)} == set(str(number))

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
    max = 0
    primes = primes_sieve(10_000_000)
    for p in primes:
        if pandigital(p,len(str(p))) and p > max:
            max = p

    return max
if __name__ == "__main__":
    
    start = default_timer()

    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop - start)
