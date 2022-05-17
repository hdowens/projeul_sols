import itertools
import math

def is_prime(n):
    if (n % 2 == 0 and n > 2) or n <= 1:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def trunc_prime_lhs(x):
    lhs_flag = True
    for i in range(0,len(str(x))-1):
        if lhs_flag:
            x = int(str(x)[1:])
            if not (is_prime(x)):
                lhs_flag = False
    if lhs_flag:
       return True
    else:
        return False

def trunc_prime_rhs(x):
    rhs_flag = True
    for i in range(0,len(str(x))-1):
        if rhs_flag:
            x = int(str(x)[:-1])
            if not (is_prime(x)):
                rhs_flag = False
    
    if rhs_flag:
       return True
    else:
        return False

lsum = 0
for i in range(10,1000000):
    if(is_prime(i)):
        try:
            if(trunc_prime_lhs(i) and trunc_prime_rhs(i)):
                lsum += i
        except:
            continue

print(lsum)
