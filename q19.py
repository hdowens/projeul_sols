"""
project euler - question 19

"""

import datetime
import calendar 



cal = calendar.Calendar()
count = 0
for i in range(1901,2001):
    for j in range(1,13):
        for day in cal.itermonthdays(i, j):
            if day == 1:
                intDay = datetime.date(year=i,month=j,day=day).weekday()
                if intDay == 6:
                    count += 1
            
print(count)       
