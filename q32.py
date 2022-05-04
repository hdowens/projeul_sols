from timeit import default_timer
from itertools import count

def is_pandigital(nums):
    if ''.join(sorted(str(nums))[0:9]) == "123456789":
        return True
    else:
        return False


def get_answer():
    lsum = set()
    for i in range(1,100):
        for j in  range(100,10000):
            if '0' not in str(i * j): 
                if(len(str(i) + str(j) + str(i*j)) == 9):
                    if(is_pandigital(int(str(i) + str(j) + str(i*j)))):
                        lsum.add(i*j)

    return sum(lsum)

if __name__ == '__main__':
    start = default_timer()
    
    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop-start)
