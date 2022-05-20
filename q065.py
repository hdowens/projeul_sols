from timeit import default_timer

"""
The formula for the numerator :
n_k = n_k-1 + n_k-2 if n_k % 3 != 0
else n_k = 2 * (k/3) * n_k-1 + n_k-2

"""

def compute():
    n0 = 2
    n1 = 3
    n2 = 8
    for i in range(4, 101):
        n0 = n1
        n1 = n2
        if i % 3 != 0:
            n2 = n1 + n0
        else:
            n2 = 2 * n1 * (i // 3) + n0
    return sum([int(x) for x in str(n2)])

if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
