"""
projeul - q29
"""

s = set()
for i in range(2,101):
  for j in range(2,101):
    s.add(math.pow(i,j))
    
print(len(s))
