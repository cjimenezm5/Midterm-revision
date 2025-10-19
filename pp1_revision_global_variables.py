#Simulate a house. The house has a mom and several kids, whenever the mom calls
#the kids have to go down to dinner, they can only come to dinner if the food is ready
#which the mom will determine and shout to the kids

import threading
import random 
import time
from concurrent.futures import ThreadPoolExecutor



food_is_ready = False

def mom():
    global food_is_ready
    print(f"I am going to cook")
    time.sleep(random.randint(1,5))
    print(f"Food is ready!")
    food_is_ready = True

def kids(name):
    global food_is_ready

    while not food_is_ready:
        time.sleep(1)
        print(f"Kid {name}: mom I'm hungry")
    print(f"Kid {name}: Coming down!")


with ThreadPoolExecutor(max_workers= 4) as executor:
    executor.submit(mom)
    for x in range(1,4):
        executor.submit(kids, x)

        
#this is the "simple" way using global and not locks

























