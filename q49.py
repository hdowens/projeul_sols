from timeit import default_timer
from sympy import sieve, isprime
from collections import Counter

def compare(list1, list2 ,list3):
    return Counter(list1) == Counter(list2) == Counter(list3)

def get_answer():
    for i in list(sieve.primerange(1450,10000)):
        for j in range(round((10000-i) / 2),1,-1):
            iter1,iter2 = i + j, i + (j * 2)
            if isprime(iter1) and isprime(iter2):
                if(compare([int(i) for i in str(i)],[int(i) for i in str(iter1)],[int(i) for i in str(iter2)])):
                    print("".join([str(i) for i in [int(i) for i in str(i)]])
                     + "".join([str(i) for i in [int(i) for i in str(iter1)]]) 
                     + "".join([str(i) for i in [int(i) for i in str(iter2)]]))
                    break

    return 1



if __name__ == "__main__":

    start = default_timer()

    get_answer()

    stop = default_timer()

    print("Time taken -> ",start - stop)
