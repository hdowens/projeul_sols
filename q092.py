from timeit import default_timer

def compute():
    count = 0
    for x in range(1, 10_000_000):
        while x != 1:
            x = sum([int(i)**2 for i in str(x)])
            if x == 89:
                count += 1
                break
    return count


if __name__ == "__main__":

    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
