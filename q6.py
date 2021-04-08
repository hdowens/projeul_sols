import math

total = 0
for x in range(1,101):
    total += x

sum_sq = pow(total,2)

sq_tot = 0
for x in range(1,101):
    sq_tot += pow(x,2)


print("diff:" ,sum_sq-sq_tot)
