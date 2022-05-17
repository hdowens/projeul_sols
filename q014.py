"""
hdwens
euler problem 14.
collatz sequence - if n is odd ->3n+1 , if n is even n/2
"""



m = 0
for i in range(5,1000000):
    l = []
    l.append(i)
    while i != 1:
        if i % 2 == 0:
            i = i // 2
            l.append(i)
        else:
            i = (3*i) + 1
            l.append(i)

        
    if len(l) > m:
        m = len(l)
        ans = l[0]



print("Longest chain is for -> ",ans," with -> ",m," steps.")
