#A toy factory runs an automated system with producer robots that make toys and inspectors who check them.
#The robots place each finished toy on a shared conveyor belt (a Python list), and the inspectors remove toys from it.
#The belt can hold a maximum of 10 toys at once.
#If it’s full, producers must wait.
#If it’s empty, consumers must wait.
#You must use a lock (threading.Lock()) to protect access to the shared belt so that only one thread can modify it at a time.
#Use time.sleep() and random to simulate different production and inspection speeds.
#Create 2 producer threads and 3 consumer threads, and have each produce or inspect 10 toys.
#Print messages showing when items are produced or consumed and the current buffer size.

import threading
import random
import time



belt = []
belt_lock = threading.Lock()
MAX_SIZE = 10

def producer(name, belt: list, belt_lock : threading.Lock):

    for i in range(10):
        time.sleep(random.random())
        toy = random.randint(10,100)
    
        with belt_lock:
            if len(belt) < MAX_SIZE :
                belt.append(toy)
                print(f"Producer {name} has produced item {toy}. Buffer size = {len(belt)}")
            
            else:
                print(f"Producer {name} is waiting, the buffer is full: {len(belt)}) / {MAX_SIZE}")

def inspector(name, belt: list, belt_lock : threading.Lock):



    for i in range(10):
        time.sleep(random.random())
        toy = random.randint(10,100)
        with belt_lock:
            if len(belt)>0:
                belt.pop(0)
                print(f"Inspector {name} has checked the item {toy}. Buffer size = {len(belt)}")
            
            else:
                print(f"Inspector {name} is waiting, the buffer is empty {len(belt)}")

producer_threads = []
inspector_threads = []

for i in range(2):  # 2 producers
    t = threading.Thread(target=producer, args=(i+1,belt, belt_lock))
    t.start()
    producer_threads.append(t)

for i in range(3):
    t= threading.Thread(target = inspector, args=(i+1,belt, belt_lock))
    t.start()
    inspector_threads.append(t)


























