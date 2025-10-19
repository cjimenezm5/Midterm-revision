#A local café has two baristas and five customers.
#Each customer places an order (which takes random time to prepare).
#Baristas must prepare the drinks in parallel, but the coffee machine can only be used by one barista at a time.


import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor


machine_lock = threading.Lock()
customer_queue = [x for x in range(1,6)]


def barista(id: int, customer_queue: list, machine_lock = threading.Lock):
    for customer in customer_queue:
        time.sleep(random.random())
        print(f"Barista {id} is preparing cutsomer's {customer} order, before the machine")

        with machine_lock:
            print(f"Barista {id} is using the coffee machine")
            time.sleep(random.randrange(1,3))
            print(f"Barista {id} finished using the machine for customer {customer}")

        print(f"Barista {id} served customer {customer}")
        time.sleep(random.random()) #wait until serving next customer.



barista_queue = []

barista_1_customers = customer_queue[:3]
barista_2_customers = customer_queue[3:]

with ThreadPoolExecutor(max_workers = 7) as executor:
    executor.submit(barista, 1, barista_1_customers, machine_lock)
    executor.submit(barista, 2, barista_2_customers, machine_lock)



























