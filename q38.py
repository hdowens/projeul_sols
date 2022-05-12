from timeit import default_timer

def is_pandigital(nums):
    if ''.join(sorted(str(nums))[0:9]) == "123456789":
        return True
    else:
        return False


def get_answer():
    lmax = 0
    for i in range(10000, 8000, -1):
        for j in range(2, 10):
            num = ""
            k = 1
            while k < j + 1 and len(num) < 9:
                num += str(k*i)
                if is_pandigital(num):
                    if int(num) > lmax:
                        lmax = int(num)
                k += 1
    return lmax

if __name__ == "__main__":
    start = default_timer()
    
    print(get_answer())

    stop = default_timer()

    print("Time taken -> ",stop-start)
