#Simulate a house. The house has a mom and several kids, whenever the mom calls
#the kids have to go down to dinner, they can only come to dinner if the food is ready
#which the mom will determine and shout to the kids

import threading
import random 
import time
from concurrent.futures import ThreadPoolExecutor


food_ready = threading.Lock()
food_ready.acquire()

def mom(food_ready : threading.Lock):
    print("I am going to start preparing the food")
    time.sleep(random.randint(1,5))
    print("Kids, the food is ready")
    food_ready.release()


def kids(id:int, food_ready : threading.Lock):

    while food_ready.locked():
        print(f"{id}: Mom I want to eat")
        time.sleep(1)
    print(f"{id}: Coming down")


with ThreadPoolExecutor(max_workers= 4) as executor:
    for i in range(1,4):
        executor.submit(kids, i, food_ready)
    executor.submit(mom, food_ready)
    





















