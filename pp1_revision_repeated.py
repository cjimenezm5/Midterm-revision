#Simulate a house. The house has a mom and several kids, whenever the mom calls
#the kids have to go down to dinner, they can only come to dinner if the food is ready
#which the mom will determine and shout to the kids



import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor

food_ready = threading.Lock()

food_ready.acquire()
def mom(food_ready: threading.Lock):
    print("Mom: kids, I am going to start preparing dinner")
    time.sleep(3)
    print("Kids, food is ready")
    food_ready.release() 


def kids(id: int, food_ready: threading.Lock):
    while food_ready.locked():
        print(f"Kid {id}: Mom I'm hungry")
        time.sleep(random.uniform(0.5,2))

    print(f"Kid {id}: Coming!")



with ThreadPoolExecutor(max_workers = 4) as executor:
    for i in range(1,4):
        executor.submit(kids, i, food_ready)
    executor.submit(mom, food_ready)



























