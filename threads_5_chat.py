#A local café has two baristas and five customers.
#Each customer places an order (which takes random time to prepare).
#Baristas must prepare the drinks in parallel, but the coffee machine can only be used by one barista at a time.



import random
import time
import threading
from concurrent.futures import ThreadPoolExecutor

machine_lock = threading.Lock()
customers = [f"Customer {i}" for i in range(1, 6)]  # 5 customers total


def barista(name, customers: list, machine_lock: threading.Lock):
    for customer in customers:
        time.sleep(random.random())  # simulate prep before using the machine
        print(f"Barista {name} is preparing the order for {customer}...")

        with machine_lock:  # only one barista can use the machine at a time
            print(f"Barista {name} is using the coffee machine for {customer}.")
            time.sleep(random.uniform(1, 3))
            print(f"Barista {name} finished using the machine for {customer}.")

        print(f"Barista {name} served {customer}!\n")
        time.sleep(random.random())  # short break before next order


# Divide customer orders between baristas
barista_threads = []

barista_1_customers = customers[:3]  # first 3 customers
barista_2_customers = customers[3:]  # last 2 customers

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(barista, 1, barista_1_customers, machine_lock)
    executor.submit(barista, 2, barista_2_customers, machine_lock)

print("All coffee orders have been prepared and served!")


























