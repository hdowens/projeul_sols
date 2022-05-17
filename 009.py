import math



"""
[]pythagorean triplets - in the form a^2 + b^2 = c ^2
[]There is a triple for which a + b + c = 1000
[]Find the product abc

Can rearrange these equations , c = 1000 - a - b
a^2 + b^2 = (1000-a-b)^2

"""
          
for i in range(0,500):
    for j in range(0,500):
        if(math.pow(i,2) + math.pow(j,2) == math.pow((1000-i-j),2)):
            print("Product: ",i*j*(1000-i-j))
