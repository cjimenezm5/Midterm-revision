#Simulate a supermarket, you have 5 different checkouts and a person has x number
#of items made randomly. They can change a checkout if another one gets free


import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

NUM_CHECKOUTS = 5
NUM_CUSTOMERS = 20

checkouts = [[] for _ in range(NUM_CHECKOUTS)]       # each checkout has its own queue
checkout_locks = [threading.Lock() for _ in range(NUM_CHECKOUTS)]  # one lock per queue
checkout_free = [True] * NUM_CHECKOUTS               # whether checkout is currently free
checkout_free_lock = threading.Lock()                # lock to protect checkout status

def customer(id: int):
    """Each customer randomly picks a checkout, waits, and may switch if another one frees up."""
    items = random.randint(1, 15)
    time.sleep(random.uniform(0.1, 0.5))  # random arrival time

    # Choose initial checkout (shortest queue)
    with checkout_free_lock:
        chosen = min(range(NUM_CHECKOUTS), key=lambda x: len(checkouts[x]))
        checkouts[chosen].append((id, items))
        print(f" Customer {id} joined checkout {chosen+1} with {items} items.")

    # While waiting, check if another checkout gets free
    while True:
        time.sleep(random.uniform(0.5, 1.5))
        with checkout_free_lock:
            # If customer is already being served, stop waiting
            if (id, items) not in checkouts[chosen]:
                return
            # Find any free checkout that has no queue
            for i in range(NUM_CHECKOUTS):
                if i != chosen and checkout_free[i] and len(checkouts[i]) == 0:
                    checkouts[chosen].remove((id, items))
                    checkouts[i].append((id, items))
                    chosen = i
                    print(f"🔄 Customer {id} switched to checkout {i+1}.")
                    break


def checkout_worker(id: int):
    """Each checkout continuously serves customers from its queue."""
    while True:
        with checkout_locks[id]:
            if len(checkouts[id]) == 0:
                # Check if all queues empty -> everyone done
                all_empty = all(len(c) == 0 for c in checkouts)
                if all_empty:
                    break
                continue

            # Serve the next customer
            customer_id, items = checkouts[id].pop(0)
            with checkout_free_lock:
                checkout_free[id] = False
            print(f"🧾 Checkout {id+1} started serving customer {customer_id} ({items} items).")

        # Simulate item scanning
        for _ in range(items):
            time.sleep(random.uniform(0.1, 0.3))

        with checkout_free_lock:
            checkout_free[id] = True
        print(f"✅ Checkout {id+1} finished customer {customer_id} ({items} items).")

        # Small pause before checking next customer
        time.sleep(random.uniform(0.1, 0.3))


# Run the simulation
with ThreadPoolExecutor(max_workers=NUM_CHECKOUTS + NUM_CUSTOMERS) as executor:
    for i in range(NUM_CHECKOUTS):
        executor.submit(checkout_worker, i)
    for i in range(1, NUM_CUSTOMERS + 1):
        executor.submit(customer, i)
