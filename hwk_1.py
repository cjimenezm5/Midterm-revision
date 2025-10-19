#queue of jobs in n=5 threads. Each job contains a number between 0-5.
#Each thread takes the next element from the queue and sleeps for x amount of seconds
#when finished, it checks for another jobs
#if tehre are no more jobs in the queue, teh thread can close itself


import random
import threading
import time

thread_count = 5

counter = 0
queue = list(lambda x: ("main", random.randrange(5), range(20)))
queue_lock = threading.Lock()
print(queue)


def jobs(name, queue : list, queue_lock: threading.Lock):
    while True:
        with queue_lock:
            if len(queue) > 0:
                task = queue.pop(0)
        
            else:
                break

        time_to_sleep = task[1]
        print (f"Thread {name} is going to sleep for {time_to_sleep} seconds")
        time.sleep(time_to_sleep)


thread_list = []
for x in range (5):
    t = threading.Thread(target = jobs, args=(x+1, queue, queue_lock))
    t.start()



