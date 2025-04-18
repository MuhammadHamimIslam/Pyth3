# to work with date and time, we need the datetime module 
import datetime

"Get the current date and time"

time = datetime.datetime.now() # returns current date andtime

print(f"Date and time is: {time}")

print(f"Current year is: {time.year}") # returns the year 

"Creating date object"

# to set time datetime.datetime(year, month, day, hour, minute, second, microsecond, timeZone)
timeSet = datetime.datetime(2025, 9, 4, 11, 44)

print(timeSet)
print(timeSet.strftime("%a"))

"strftime() method"

"""takes a parameter
 %a -> weekday (short form)
 %A -> weekday (full form)
 %w -> dayNumber (0-6) Sunday is 0
 %d -> dayMonth (0-31)
 %j -> dayNumberYear (0-365)
 %B -> monthName 
 %Y -> Year (full form)
 %H -> Hour (0-23)
 %I -> Hour (0-12)
 %p -> AM/PM
 %Z -> timeZone
 %M -> Minutes 
 %a -> Seconds
"""
