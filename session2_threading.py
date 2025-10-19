import threading
import random
import sys
import time

#Write an application that handles a queue of jobs in N=5 threads. Each job
#contains a number between 0-5. Each thread takes the next element from the
#queue and sleeps for the given amount of second (as an imitation of actual work
#it should be doing). When finished it checks for another job. If there are no more
#jobs in the queue, the thread can close itself.

thread_count = 5

counter = 0
queue= list(map(lambda x: ("main", random.randrange(5)), range(20)))
locker = threading.Lock()

class ThreadedCount(threading.Thread):
    def run(self):
        global counter
        my_counter =0
        thread = threading.current_thread()
        print('{} - start thread'.format(thread.name))
        while (True):
            locker.acquire()
            job= None
            if len(queue) > 0:
                counter +=1
                my_counter += 1
                job = queue[0]
                queue[0:1] = []
            locker.release()
            if job == None:
                print('{} - no more jobs'.format(thread.name))
                break

            print('{} - working on job {} ({}) from {} sleep for {}'
                .format(thread.name, counter, my_counter , job[0], job[1]))
            time.sleep(job[1])
        return

threads = []
for i in range(thread_count):
    threads.append(ThreadedCount())
for t in threads:
    t.start()
for t in threads:
    t.join()
