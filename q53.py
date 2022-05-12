from timeit import default_timer
from math import factorial

def nCr(n, r):
    return factorial(n) // factorial(r) // factorial(n-r)

def compute():
    return len([r for n in range(1,101) for r in range(1, n + 1) if nCr(n,r) > 1_000_000])
    
if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
