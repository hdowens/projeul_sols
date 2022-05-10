from timeit import default_timer
from itertools import permutations

def substring(x):
    ret = True
    if int(x[1:4]) % 2 != 0:
        ret = False
    if int(x[2:5]) % 3 != 0:
        ret = False
    if int(x[3:6]) % 5 != 0:
        ret = False
    if int(x[4:7]) % 7 != 0:
        ret = False
    if int(x[5:8]) % 11 != 0:
        ret = False
    if int(x[6:9]) % 13 != 0:
        ret = False
    if int(x[7:10]) % 17 != 0:
        ret = False 
    return ret


def get_answer():
    lmax = 0
    perm_list = ["".join(num) for num in permutations("0123456789")]
    for num in perm_list:
        if substring(num):
            lmax += int(num)
    return lmax

if __name__ == "__main__":
    start = default_timer()
    
    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop-start)
