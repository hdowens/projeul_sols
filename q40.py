import timeit

def champernownes():
    return "".join([str(i) for i in range(1000001)])

def get_answer():
    c = champernownes()
    return int(c[1]) * int(c[10]) * int(c[100]) * int(c[1000]) * int(c[10000]) * int(c[100000]) * int(c[1000000])


if __name__ == '__main__':
    start = timeit.default_timer()
    
    print(get_answer())

    stop = timeit.default_timer()

    print("Time taken -> ",stop-start)
