from timeit import default_timer
from math import sqrt

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes_sieve_primelim(limit):
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
    primes = primes_sieve_primelim(3940)
    ans,consec_max = 0,0
    for i in range(len(primes)):
        sum = primes[i]
        consec = 1
        for j in range(i + 1, len(primes)):
            sum += primes[j]
            consec += 1
            if is_prime(sum) and consec > consec_max:
                ans = sum
                consec_max = consec

    //print("LONGEST SUM IS -> ", ans, "with this many digits -> ",consec_max)
    return ans




if __name__ == "__main__":
    
    start = default_timer()

    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop - start)
