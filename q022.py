"""
q22 - names scores

"""
import csv

def letter_to_val(l):
    alphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
    return alphabet.index(l.lower()) + 1
    
tmp=[]
names=[]
with open('names.txt', 'r') as filename:
    file_data = csv.reader(filename, delimiter=',')
    tmp = list(file_data)

for i in tmp[0]:
    names.append(i)
   
sortednames = sorted(names)

lsum = 0

for i in range(0,len(sortednames)):
    val = 0
    for j in sortednames[i]:
        val += letter_to_val(j)
    val *= i+1
    lsum += val
    
print(lsum)

