from timeit import default_timer

def find_amount():
    amount = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * 201
    ways[0] = 1

    for i in range(0, len(coins)):
        for j in range(coins[i], amount+1):
            ways[j] += ways[j - coins[i]]

    return(ways[200])

if __name__ == '__main__':
    start = default_timer()
    
    print(find_amount())

    stop = default_timer()

    print("Time taken -> ",stop-start)
