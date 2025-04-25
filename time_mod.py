import time

ticks = time.time()
print(ticks) # returns the current system time in  ticks since 12:00am, January 1, 1970(epoch)
"time.asctime([t])"

t = time.asctime()


"format the time"

localTime = time.asctime(time.localtime()) # returns the local time and date
print(localTime)





