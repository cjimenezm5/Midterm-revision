#1:Simulate a house. The house has a mom and several kids, whenever the mom calls
#the kids have to go down to dinner, they can only come to dinner if the food is ready
#which the mom will determine and shout to the kids


import time
import random 
from concurrent.futures import ThreadPoolExecutor

is_food_ready = False

def mom():
    global is_food_ready
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
    executor.submit(mom)
    for x in range(1,4):
        executor.submit(kid, x)
        
#this is the "simple" way using global and not locks
















