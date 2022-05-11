from math import pow

print("diff:" ,pow(sum(x for x in range(1,101)),2)-sum(pow(x,2) for x in range(1,101)))
