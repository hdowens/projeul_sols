import itertools
next = 1
current = 0
for i in itertools.count():
    if len(str(current)) == 1000:
        print("Answer occuring at INDEX -> ",i)
    next, current = current, next + current
    
