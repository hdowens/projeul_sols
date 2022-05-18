from timeit import default_timer
from collections import Counter
from itertools import count

def compare(list1, list2):
    return Counter(list1) == Counter(list2)
"""
defintely the ugliest solution to date. Runs in < 1s though so I feel no need to optimise it.
yes, you could make sure it only iterates over numbers which will produce a 6x which still is
the same length, i.e. only 100 -> 166, 1000-1666 etc. Maybe if this appears in a later 
problem I will.

Interestingly, after reading through other solutions, the number is itself an interesting property.
In the deciaml representation of 1 / 7, we have 0.142857 142857 142857 ...
and 7 x 0.142857 = 0.99999
So the answer shows up in other places too.
"""
def compute():
    for x in count(1):
        x_list = [int(x) for x in str(x)]
        x2_list = [int(x) for x in str(x * 2)]
        x3_list = [int(x) for x in str(x * 3)]
        x4_list = [int(x) for x in str(x * 4)]
        x5_list = [int(x) for x in str(x * 5)]
        x6_list = [int(x) for x in str(x * 6)]
        if compare(x_list, x2_list):
             if compare(x_list, x3_list):
                 if compare(x_list, x4_list):
                     if compare(x_list, x5_list):
                         if compare(x_list, x6_list):
                             print("Ans -> ", x)
                             return x
                              

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
