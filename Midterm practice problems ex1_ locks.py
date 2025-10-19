#1:Simulate a house. The house has a mom and several kids, whenever the mom calls
#the kids have to go down to dinner, they can only come to dinner if the food is ready
#which the mom will determine and shout to the kids


#NOT FINISHED, ASK CHAT/ LOOK FOR ANSWER ON BB

import time
import random 
from concurrent.futures import ThreadPoolExecutor
import threading

is_food_ready = threading.Lock()

def mom(is_food_ready:threading.Lock):
    while not is_food_ready:
        print("I am going to cook")
        time.sleep(random.randint(1,5))
        print("Food is ready")
        is_food_ready = True


def kid(id):
    global is_food_ready
    while not is_food_ready:
        time.sleep(1)
        print(f"Kid {id}: Mom I am hungry")
    print(f"Kid {id}: going for lunch")

with ThreadPoolExecutor(max_workers=4) as executor:
    for x in range(1,4):
     executor.submit(mom)
    

















