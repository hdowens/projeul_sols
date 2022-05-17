import math

total = 1

for i in range(2,20):
    x = total
    y = i
    gcd = math.gcd(int(x),int(y))
    lcm = ( x * y ) / gcd
    total = lcm

print(total)
        
