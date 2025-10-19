#An airport has a luggage conveyor belt that can hold a maximum of 10 bags.
#Airline staff (producers) keep adding luggage to the belt, while passengers (consumers) remove them when they arrive.
#Simulate the process ensuring the belt never exceeds its capacity and never goes below zero.


import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor



max_capacity = 10
belt = []
belt_lock = threading.Lock()


def producers(id:int, belt_lock : threading.Lock, belt: list ):
        
        for i in range(1,16):
            time.sleep(1)
            bag = random.randint(100,1999)

            with belt_lock:
                    if len(belt)<max_capacity:
                        belt.append(bag)
                        print(f"Staff {id} has added item {i} to the belt")
                    else:
                        print(f"Staff {id} is waiting to add more luggage, conveyor belt is full")


def passengers(id:int, belt_lock : threading.Lock, belt:list):

     for i in range(1,11):
        time.sleep(1)
        with belt_lock:
            if len(belt)>0:
                bag = belt.pop(0)
                print(f"Passenger {id} has removed their luggage {bag}")
            else:
                print(f"Passenger {id} is waiting, no more lugage on the belt")


with ThreadPoolExecutor(max_workers = 5) as executor:
    for i in range(3):
          executor.submit(passengers, i+1, belt_lock, belt )
    for i in range(2):
        executor.submit(producers, i+1, belt_lock, belt)          
     
              
print("All luggage has been collected")











