# CH9A - calling modules from separate files
#This script will serve as the main program where you will combine all the elements of the project

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
    
#______________________________Section 4_______________________________________
# Timestamp is the difference between a particular date and January 1st 1970, 00:00:00 UTC and is expressed in seconds
timestamp = time.time()
print("Timestamp:", timestamp)

d = dt.fromtimestamp(timestamp)
print("Date:", d)

#______________________________Section 5_______________________________________
d = dt(2019, 11, 4)
print(d.weekday())