from email.policy import default
from timeit import default_timer

def compute():
    return ((28433 * 2 ** 7830457 + 1) % (10**10))


if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
