from timeit import default_timer

def generate_pentag_nums(lim):
    return [((3*(n**2)) - n) // 2 for n in range(1,lim)]

def get_answer():
    nums = generate_pentag_nums(10001)
    for i in nums:
        for j in nums:
            if i + j in nums and  abs(i - j) in nums:
                    print(abs(i-j))
                    break
    
if __name__ == "__main__":
    start = default_timer()
    
    get_answer()

    stop = default_timer()

    print("Time taken -> ",stop-start)
