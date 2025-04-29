import calendar 

"""calendar.calendar(year, w=2, l=1, c=6, m=3)

w -> width of each column 
l -> line numbers of per week 
c -> spaces between month columns 
m -> The number of rows per month 
"""

print(calendar.calendar(2025)) 

"calendar.isleap(year)"

print(calendar.isleap(2025)) # returns if the year is leap year

"calendar.leapdays(year1, year2)"
print(2000, 2025) # returns number of leap years between the given years (excluding the end year).

"calendar.month(year, month, w=2, l=1)"

print(calendar.month(2025, 4)) # returns the calendar of the give month 