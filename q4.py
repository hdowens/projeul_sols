

def palindrome_test(s):
    s = str(s)
    return len(s) < 2 or ( s[0] == s[-1] and palindrome_test(s[1: -1]))

one = 999
two = 999
tot = 0

for i in range(999,0,-1):
    for j in range(999,0,-1):
        pro = i * j
        if(pro > tot and palindrome_test(pro)):
            print("total found of: ", i," x ",j)
            tot = pro


print(tot)
        

