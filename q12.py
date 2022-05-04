from math import sqrt
import timeit

def div(n):
    lst = list()
    for i in range(1,int(sqrt(n))):
        if n % i == 0:
            lst.append(i)
            lst.append(n//i)
    return lst

def get_answer():
    i = 2
    n = 1
    while True:
        if len(div(n))> 500:
            return n
        n = i+n
        i+=1

if __name__ == "__main__":
    start = timeit.default_timer()
    
    print(get_answer())

    stop = timeit.default_timer()

    print("Time taken -> ",stop-start)
