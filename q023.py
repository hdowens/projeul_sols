
import itertools
abun_nums = []

def is_abundant(n):
    ret = 1
    for i in range(2,int(n/2)+1):
        if n % i == 0:
            ret += i
    return ret > n

for i in range(11,28124):
    if(is_abundant(i)):
        abun_nums.append(i)

nums = {i:False for i in range(0,28124)}

for i in abun_nums:
    for j in abun_nums:
        if i + j < 28124:
            nums[i+j] = True

lsum = 0
for key in nums.keys():
    if not nums[key]:
        lsum += key

print(lsum)
