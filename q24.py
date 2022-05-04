from itertools import permutations
from timeit import default_timer

def lexico_perms(x):
    perms = [x for x in permutations(x)]
    return perms[999999]
    

def get_answer():
    return(lexico_perms("0123456789"))


if __name__ == "__main__":

    start = default_timer()
    
    print(''.join(get_answer()))

    stop = default_timer()

    print("Time taken -> ",stop-start)
