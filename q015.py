"""
q15- lattice paths

I understood this question to be a combinatoric problem. We can either have R
or D in the string. The formula

"""
def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)

num = fac(40)

num = num // (fac(20) * fac(20))

print(num)
