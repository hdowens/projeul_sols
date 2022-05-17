from timeit import default_timer

def find_amount():
    ways = [0] * 101
    ways[0] = 1

    for i in range(1, 100):
        for j in range(i, 101):
            ways[j] += ways[j - i]

    return(ways[100])

if __name__ == '__main__':
    start = default_timer()
    
    print(find_amount())

    stop = default_timer()

    print("Time taken -> ",stop-start)
