from timeit import default_timer
from math import sqrt

def is_pentagonal(n):
    n = (sqrt(1 + 24*n)+1)/6
    return n.is_integer()

def get_answer():
    for i in range(144,99999):
        n = i * (2 * i - 1)
        if isPentagonal(n):
            print(n)

if __name__ == "__main__":
    
    start = default_timer()

    get_answer()

    stop = default_timer()

    print("Time taken -> ",stop - start)
