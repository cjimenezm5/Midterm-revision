#Carmen Jiménez Montosa

import threading
import random
import time
import concurrent.futures
import logging

thread_count = 5

counter = 0
queue= list(map(lambda x: ("main", random.randrange(5)), range(20)))
locker = threading.Lock() #protects global and thread counters

def thread_function(job): #function done by pool threads for each job
    global counter
    thread = threading.current_thread() #get current thread

    #only first task run by this thread prints start
    if not hasattr(thread, "my_counter"):  #if this pool worker hasn't seen any job yet, initalise its per thread job counter
        thread.my_counter = 0
        print(f"{thread.name} - start thread") #log that the worker started
    
    #update shared and per thread counters
    with locker:    #acquire the lock, inrceement thread count and show global and local count
        counter += 1
        thread.my_counter += 1
        global_count = counter
        my_counter= thread.my_counter

    
    print(f"{thread.name} - working on job {global_count}({my_counter})"
          f"from {job[0]} sleep for {job[1]}")
    time.sleep(job[1])

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers = thread_count) as executor:
        for job in queue:      #submit 1 task per pool, pool schedules accross the 5 workers
            executor.submit(thread_function, job) #exiting thr "with" waits for all submitted tasks to finish and then shuts the pool down. 


    print("All jobs have been processed.")
    