"""
problem 17 - numbers one to 1000
everytime a one is read, 3 to the count
2 - 3, 3 - 5, 4 - 4, 5 - 4, 6 - 3,7- 5, 8 - 5, 9 - 4
11 - 6, 12 - 6, 13 - 8, 14 - 8, 15 - 7, 16 - 7, 17 - 9, 18 - 8, 19 - 8
20 - 6(+1 for every twenty number there is a hyphen)
30 - 6 
40 - 5 
50 - 5
60 - 5 
70 - 7 
80 - 6 
90 - 6 

every hundred 7 + 3(3 for the and)
100 - 3
200 - 3 
300 - 5
400 - 4
500 - 4
600 - 3
700 - 5
800 - 5
900 - 4
1000 - 3 + 8
three hundred and forty-two
5     7       3   5    1 3
the only way is to brute force
"""

#1-9
total = 3+3+5+4+4+3+5+5+4
#11-19
total += 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
#20-99
total += (8*36) + 10*(6 + 6 + 5 + 5 + 5 + 7 + 6 +6)
#100-999
total += (36*100) + (9*854) + (7*9) + 8910
#1000
total+= 3 + 8

print(total)
