from timeit import default_timer
from sympy import totient
from collections import Counter
from sympy import sieve
from itertools import combinations
   


def compare(list1, list2):
    return Counter(list1) == Counter(list2)


#with absolutely no optimisation
#very slow
def compute_bruteforce():
    return min([[i/totient(i), i] for i in range(10,10_000_001) if compare([int(x) for x in str(i)], [int(x) for x in str(totient(i))])])

#test to see if faster than counter
def is_perm(n1, n2):
    return sorted(str(n1)) == sorted(str(n2))


"""
Explanation of code:

We know that when phi(n) is nearly n that n / phi(n) is going to be minimised.
When is phi(n) near n ? When there are as few small primes involved as possible, we need

(Remember phi(n) must be < n)

We know that phi(p) = p - 1 for each prime number p. It follows that p and p - 1 can never
be permutations of each other. Therefore, we need to find prime composites. 
phi(p1p2) = p1p2 * (1 - 1/p1)*(1-1/p2) = (p1 - 1)*(p2 - 1)

So for our answer n we have phi(n) = (p1 - 1)(p2 - 1). As stated before we need this to be
as close to n as possible to produce a minimum. If that is true, then we know that p1 and p2
must be close to sqrt(n) as we know at max p1 * p2 ≈ n. So we only need to search primes up to 
sqrt(n).

"""
def compute_withlogic(LIMIT = 10 ** 7):
    prime_list = sieve.primerange(2 * int(LIMIT ** 0.5))
    min_ratio = LIMIT ** 0.5
    ans = 0
    for p1, p2 in combinations(prime_list, 2):
        if p1 * p2 < LIMIT:
            n = p1 * p2
            tot = (p1 - 1) * (p2 - 1)
            if (n / float(tot)) < min_ratio and is_perm(n, tot):
                ans = n
                min_ratio = (n / float(tot))


    print("Num -> ", ans, "\tratio -> ", min_ratio)
    return ans


if __name__ == "__main__":

    start = default_timer()

    print(compute_withlogic())

    stop = default_timer()

    print("Time taken -> ", stop - start)
