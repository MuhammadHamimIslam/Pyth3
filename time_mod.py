import time

"Epoch means starting time which is "

print(time.time()) # returns the current system time from Epoch 
"time.asctime([t])"

t = time.asctime() # returns current time
print(t)

"format the time"

localTime = time.asctime(time.localtime()) # returns the local time and date
print(localTime)

print(time.ctime(60)) # converts the time 60 seconds after the Epoch
print(time.gmtime(60))

print(time.localtime()) # returns the local time 

time.sleep(2) # program stops for 2 seconds
print("Restarted after 2 seconds!")

# checks how much time it take to perform a work 
start = time.perf_counter() # start counting 
time.sleep(1) # take 1 second 
stop = time.perf_counter() # stop counting 
print(f"It took {stop - start} seconds")

# check how much time(CPU Time) it took to do a work 
startCount = time.process_time() # starts counting 
time.sleep(1) # it isn't be counted as CPU Time 
stopCount = time.process_time()
print(f"It took {stopCount - startCount} seconds")
