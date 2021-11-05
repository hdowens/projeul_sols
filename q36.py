def palin(x):
    x= str(x)
    return len(x) < 2 or ( x[0] == x[-1] and palin( x[1:-1]))

def dec_to_bin(x):
    return "{0:b}".format(x)

lsum = 0
for i in range(0,1000001):
    if(palin(i) and palin(dec_to_bin(i))):
        lsum += i

print(lsum)
