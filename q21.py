import math


#project euler - q21 - amicable numbers

def d(n):
    isum = 0
    divs = {1}
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.update((i,n//i))
    for i in divs:
        isum += i
    return isum



li = []
for i in range(1,10001):
    s = d(i)
    if d(s) == i and s != i:
        if i not in li and s not in li:
            li.append(i)
            li.append(s)
            print("Amicable sum of ->",i, "->",s)
    
su = 0    
for i in li:
    su += i
    
print(su)
