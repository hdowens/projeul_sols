from timeit import default_timer
from sympy import prime

"""
I initially tried brute forcing which was ridiculously slow. I then tried changing the 
ranges of the loops to see how long they would individually take, and I noticed that
the max below 5000 was 2310, the max below 50000 was 30030. I recognised these numbers

2310  = 2 * 3 * 5 * 7 * 11
30030 = 2 * 3 * 5 * 7 * 11 * 13

So I tried the next prime, 

2 * 3 * 5 * 7 * 9 * 11 * 13 * 17 = 510510

I solved this on paper after I realised what the numbers were,
but I wrote a program to solve it also, it simply sums primes until 
the next prime multiplied would make it above 1,000,000

"""

def compute():
    count, lsum = 0, 1
    while lsum < 1_000_000:
        count += 1
        lsum *= prime(count)

    return lsum / prime(count)



if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()  
    
    print("Time taken -> ", stop - start)
