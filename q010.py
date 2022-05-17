
"""
project euler q10 - summation of primes
sum of primes below 10 is 2 + 3 + 5 + 7 = 17
find the sum of primes below 2,000,000

"""


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

print(sum(primes_sieve(2000000)))
