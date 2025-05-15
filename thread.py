import threading 
import time 

# a function that represents some task is going
def doSomething(sec, thread_name): 
    print(f"doing something! for {thread_name}")
    time.sleep(sec)
    print(threading.current_thread().name) # get the current thread's name



# general code without thread (code runs a work after a work)
count1 = time.perf_counter()


doSomething(3, "1")

doSomething(2, "2")
doSomething(1, "3")

count2 = time.perf_counter()
print("It took {time} seconds to run the code".format(time= count2 - count1)) # checking how much of time it took 


# using thread (code runs in the background multiple tasks at the same time )
count3 = time.perf_counter()

t1 = threading.Thread(target=doSomething, args=[3, 1], name="thread1") # defining a thread 
t2 = threading.Thread(target=doSomething, args=[2, 2])
t2.name = "thread2" # assigning name
t3 = threading.Thread(target=doSomething, args=[1, 3])

# calling thread to start 
t1.start() # start thread 
t1.join() # join thread -> wait for it to complete then go to the next

t2.start()
t2.join()

t3.start()
t3.join()

count4 = time.perf_counter()
print("It took {time} seconds to run the code".format(time= count4 - count3)) # checking how much of time it took