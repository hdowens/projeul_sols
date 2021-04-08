count = 9593
for i in range(99991,1100000):
    p = True
    for j in range(2,i):
        if(i%j == 0):
            p = False
    if(p):
        count += 1
        print("PRIME NO: ",count," : ",i)
        
