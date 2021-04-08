def fac(n):
    if n == 1:
        return 1
    else:
        return n*fac(n-1)



n = fac(100)
s = 0
for i in str(n):
    s += int(i)

print(s)
