from timeit import default_timer

def get_answer():
    print(str(sum(int(x**x) for x in range(1,1001)))[-10:])

if __name__ == "__main__":

    start = default_timer()

    get_answer()

    stop = default_timer()

    print("Time taken -> ",stop - start)
