from timeit import default_timer

def dig_sum(x):
    return sum([int(n) for n in str(x)])

def compute():
    return max([ dig_sum(int(a**b)) for a in range(1, 101) for b in range(1,101)])

if __name__ == "__main__":
      
    start = default_timer()

    print(compute())

    stop = default_timer()

    print("Time taken -> ", stop - start)
