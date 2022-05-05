from timeit import default_timer
from math import sqrt, pow

def right_angle_tr(lim):
    perim_list = [0 for i in range(1, lim)]
    for i in range(1, lim):
        for j in range(i, lim):
            hypot = sqrt(pow(i,2) + pow(j,2))
            if hypot == int(hypot) and int(i+j+hypot) < lim:
                perim_list[int(i+j+hypot)] += 1
                
    return perim_list.index(max(perim_list))
    

if __name__ == "__main__":
    start = default_timer()
    
    print(right_angle_tr(1000))

    stop = default_timer()

    print("Time taken -> ",stop-start)
