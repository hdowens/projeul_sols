from timeit import default_timer

def rect_count(a, b):
    return ((a * (a + 1) * b * (b + 1) )) // 4

def compute():
    lmin = 1000000
    n1, n2 = 0,0
    for a in range(2, 100):
        for b in range(3, 100):
            if abs(2_000_000 - rect_count(a, b)) < lmin:
                lmin = abs(2_000_000 - rect_count(a, b))
                n1, n2 = a, b
    return lmin, n1 * n2

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
