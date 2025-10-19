import concurrent.futures
from random import random, randrange
import time
import logging
import threading


def thread_function(name):
    print(f"Thread {name} is starting")
    time_sleeping = randrange(10)
    print(f"Thread {name} will sleep for {time_sleeping} seconds")
    time.sleep(time_sleeping)
    print(f"Thread {name} is finishing")


if __name__ == "__main__":
    format = "%(astime)s: %(message)a"
    logging.basicConfig(format = format, level = logging.INFO, datefmt = "%H:%M:%S")

with concurrent.futures.ThreadPoolExecutor(max_workers = 3) as executor: #this way you don't have to manually create the threads 
    executor.map(thread_function, range(3)) #submits multiple tasks to teh thread pool




#the with executor waits for all threads to finish, it joins threads and shuts down the pool
















