from timeit import default_timer
from math import sqrt, pow

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def golbach_conj(num):
    for i in range(1,101):
        if is_prime(num - ( 2 * pow(i,2))):
            return False
    return True

def get_answer():
    count = 9
    while True:
        if not is_prime(count):
            if golbach_conj(count):
                print("Num found -> ",count)
                return count
        count += 2
        
if __name__ == "__main__":
    
    start = default_timer()

    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop - start)
