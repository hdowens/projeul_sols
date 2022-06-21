from timeit import default_timer

"""
we know that any num raised to a power >= 10 will be false
so first loop is 1 throught 9
second loop is just a optimised guess, 100 runs in 0.0008s so I feel no need to change it.

"""


def compute():
    count = 0
    for x in range(1, 10):
        for exp in range(1, 100):
            if len(str(x ** exp)) == exp:
                count += 1
    return count

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
