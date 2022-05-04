from timeit import default_timer
from itertools import count
from math import pow



#used google here to try and find a limit on what the range could be
#ended up finding a formula that stats the limit is (n+1) * (9**n) which is valid for 0 < n < 35
#and as our power is 5, I subbed it in and it it was much quicker.
def find_lim(n):
    return (n+1) * pow(9,n)

def digit_powers(power):
    ans = 0
    for i in range(2,int(find_lim(power))):
        if i == sum(int(x)**power for x in str(i)):
            ans += i    
    return ans


if __name__ == "__main__":

    start = default_timer()
    
    print(digit_powers(5))  

    stop = default_timer()

    print("Time taken -> ",stop-start)
