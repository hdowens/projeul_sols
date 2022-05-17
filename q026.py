def multOrd(n):
    tmp = 1
    while 10 ** tmp % n != 1:
        tmp += 1
    return tmp

localmax = 0
localind = 0
for i in range(2,1000):
    if i % 2 == 0 or i % 5 == 0:
        continue
    else:
        length = multOrd(i)
        if length > localmax:
            localmax = length
            localind = i

print("Ans is -> ",localind)
