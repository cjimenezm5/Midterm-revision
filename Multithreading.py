import logging
import threading
import time
from random import *



def thread_function(name):
    print(f"Thread {name}: starting")
    time_sleeping = randrange(10)
    print(f"Thread {name} will sleep for: {time_sleeping}")
    time.sleep(time_sleeping)
    print(f"Thread {name} finishing")


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s" #print time of message, then ":" and then the message
    logging.basicConfig(format = format, level = logging.INFO, 
                        datefmt="%H:%M:%S") 
    
    threads = list()
    for i in range(30):
        print(f"Main : create and start thread {i}.")
        x = threading.Thread(target = thread_function, args = (i,))
        threads.append(x)
        x.start()   #begins execution in parallel
    
    for i, thread in enumerate(threads):    #Loop over each thread
        print(f"Main: before joining thread {i}")
        thread.join()   #main thread waits for each thread to finish one by one
        print(f"Main: thread {i} done!")
#this last part makes sure that things are done in order, thread 0 starts and finishes before the other threads