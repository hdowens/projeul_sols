from timeit import default_timer
from math import sqrt
from itertools import count
from sympy import primefactors

def factors(num):
    num_facs = set()
    while num != 1:
        for i in range(2, int(num + 1)):
            if num % i == 0:
                num /= i
                num_facs.add(i)
                break
    prime_facs = filter(is_prime, num_facs)
    return prime_facs

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def attempt1():
    for i in count(646):
        prime_facs = list(factors(i))
        if len(prime_facs) == 4:
            one = list(factors(i+1))
            two = list(factors(i+2))
            three = list(factors(i+3))
            if len(one) == 4 and len(two) == 4 and len(three) == 4:
                print("Found, with numbers ", i , i + 1, i + 2, i + 3)
                return i

def attempt2():
    for i in range(646,200000):
        if len(primefactors(i)) == 4:
            if len(primefactors(i+1)) == 4 and len(primefactors(i+2)) == 4 and len(primefactors(i+3)) == 4:
                return(i)
                break


if __name__ == "__main__":

    start = default_timer()

    print(attempt2())

    stop = default_timer()

    print("Time taken -> ",stop - start)
