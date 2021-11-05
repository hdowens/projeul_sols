import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def shift(n):
    l = list(str(n))
    if len(l) == 1:
        if n == 2 or n == 3 or n == 5 or n == 7:
            return n
    tmp = l[len(str(n))-1]
    l[len(str(n))-1] = l[0]
    for j in range(0,len(l)): 
        if(j == len(l) - 2):
            l[len(l)-2] = tmp
        elif j < len(l)-2:
            l[j] = l[j+1]    
    s = [str(integer) for integer in l]
    a = "".join(s)
    return a


circ_counter = 0
for i in range(2,1000001):
    ret = []
    for j in range(0,len(str(i))):
        ret.append(i)
        i = shift(i)
        
    flag = True
    for x in ret:
        if not is_prime(int(x)):
            flag = False
        
    if flag:
        circ_counter += 1

print(circ_counter)
