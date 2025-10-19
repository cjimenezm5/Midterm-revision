import concurrent.futures
import logging
from random import random, randrange
import threading
import time

def thread_function(name):
    print(f"Thread {name}: starting")
    time_sleeping = randrange(10)
    print(f"Thread {name} will sleep for: {time_sleeping}")
    time.sleep(time_sleeping)
    print(f"Thread {name} finishing")

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        for x in range(16):
            executor.submit(thread_function,x)
        #executor.map(thread_function, range(8))
    print("I am finished")