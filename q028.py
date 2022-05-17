from timeit import default_timer
from math import pow

def spiral_matrix_sum(n):
    
    #in the 5 by 5 spiral we know that the top right hand side
    #number is the last, so that is the limit to our loop
    limit = n * n

    #lsum is the var keeping track of the sum
    #step is at 2 which is the current jump between numbers to be added to the sum (3,5,7,9)
    #but every 4 numbers the jump increases by 2, e.g. (13,7,21,25) are the next ones.
    #so when count is a multiple of 4, step will increase by 2.

    lsum , step, count, iter = 1, 2, 0, 3
    while iter <= limit:
        lsum += iter
        count += 1
        if count % 4 == 0:
            step += 2
        iter += step
    return lsum


if __name__ == "__main__":

    start = default_timer()
    
    print(spiral_matrix_sum(1001))

    stop = default_timer()

    print("Time taken -> ",stop-start)




