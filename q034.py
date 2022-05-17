from timeit import default_timer
from math import factorial
from timeit import default_timer

def digit_fac(n):
    return sum(factorial(int(i)) for i in list(str(n)))


def find_nums():
    return sum(i for i in range(3,230000) if digit_fac(i) == i)
    


if __name__ == "__main__":
    start = default_timer()
    
    print(find_nums())

    stop = default_timer()

    print("Time taken -> ",stop-start)
