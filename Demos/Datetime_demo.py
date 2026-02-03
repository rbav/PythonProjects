#Demo of datetime & relevant modules
#______________________________Section 1_______________________________________
from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import time

#______________________________Section 2_______________________________________
current_time = dt.now()

print("The date is", current_time.year, "C.E.", current_time.month, "month", current_time.day, "day")
print("The time is", current_time.hour, "hours", current_time.minute, "minutes", current_time.second, "seconds")

#______________________________Section 3_______________________________________

today = dt.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)
print("Hour:", today.hour)
print("Minute:", today.minute)
print("Second:", today.second)
print("Microsecond:", today.microsecond)
    
#______________________________Section 4_______________________________________
# Timestamp is the difference between a particular date and January 1st 1970, 00:00:00 UTC and is expressed in seconds
timestamp = time.time()
print("Timestamp:", timestamp)

d = dt.fromtimestamp(timestamp)
print("Date:", d)

#______________________________Section 5_______________________________________
#This code checks what day of the week a certain date was. Monday = 0, Sunday = 6
d = dt(2025, 11, 3)
print(d.weekday())
print(d.isoweekday()) #same as weekday() but Monday = 1, Sunday = 7

#______________________________Section 6_______________________________________
#Converts time (since Jan 1st 1970) to a string
print(time.ctime(timestamp))

#______________________________Section 7_______________________________________
#Difference between datetimes
d1 = dt(2020, 11, 4)
d2 = dt(2019, 11, 4)

print(d1 - d2)

dt1 = dt(2020, 11, 4, 0, 0, 0)
dt2 = dt(2019, 11, 4, 14, 53, 0)

print(dt1 - dt2)

#______________________________Section 8_______________________________________
# Uses the calendar module and displays the calendar for the whole year
import calendar
#print(calendar.calendar(2026))

# calendar.prcal(2020) #alternative method for above line
#calendar.prcal(2020) 

#Displays specific month only
print(calendar.month(2026, 11))

#method to show calendar with sunday on the left hand side as the first day (USA method)
calendar.setfirstweekday(calendar.SUNDAY)
calendar.prmonth(2026, 12)
    