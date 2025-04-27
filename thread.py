import threading 
import time 

# a function that represents some task is going
def doSomething(sec): 
    print("doing something!")
    time.sleep(sec)


# general code without thread (code runs a work after a work)
count1 = time.perf_counter()

doSomething(3)
doSomething(2)
doSomething(1)

count2 = time.perf_counter()
print("It took {time} seconds to run the code".format(time= count2 - count1)) # checking how much of time it took 


# using thread (code runs in the background multiple tasks at the same time )
count3 = time.perf_counter()

t1 = threading.Thread(target=doSomething, args=[3]) # defining a thread 
t2 = threading.Thread(target=doSomething, args=[2])
t3 = threading.Thread(target=doSomething, args=[1])

# calling thread 
t1.start()
t2.start()
t3.start()

count4 = time.perf_counter()
print("It took {time} seconds to run the code".format(time= count4 - count3)) # checking how much of time it took 
