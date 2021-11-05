from functools import reduce
import time
start = time.time()
n = 1
list_divs = []
while len(list_divs) < 500:
    tri_n = (n*n+n)/2 # Generates the triangle number T(n)
    list_divs = list(set(reduce(list.__add__,([i, int(tri_n//i)] for i in range(1, int(pow(tri_n, 0.5) + 1)) if tri_n % i == 0)))) # this is the factor generator for any number n
    n+=1
print(tri_n, time.time() - start)
