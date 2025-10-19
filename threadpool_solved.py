import threading
import random
import time
import concurrent.futures
import logging

thread_count = 5

counter = 0
queue= list(map(lambda x: ("main", random.randrange(5)), range(20))) #20 threads, each with 2 tupples
queue_lock = threading.Lock()
print(queue)


def threadpool_processor(name,queue:list, queue_lock:threading.Lock): #needs the tupples, thus, put the list. You pass a reference (the queue)
    while True:
        with queue_lock: #to protect it
            if len(queue)> 0: #to make sure the queue isn't empty
                task = queue.pop(0) #to get the first element in the queue
            else:
                break


        time_to_sleep=task[1]
        print(f"Thread {name} is going to sleep {time_to_sleep} seconds")
        time.sleep(time_to_sleep)

thread_list = []
for x in range (5):
    t = threading.Thread(target = threadpool_processor, args=(x+1, queue, queue_lock))
    t.start()

#There were 6 threads running, the main thread + the 5 threads we created.





















