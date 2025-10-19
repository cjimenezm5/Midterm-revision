import threading
from concurrent.futures import ThreadPoolExecutor
import time
import random

#We have a class with 50 students and two teachers. Students will randomly decide to
#raise their hand and teachers will call them and they will give a presentation of 5
#seconds. A student may decide to lower their hand but the teacher will call a person
#they haven’t called if no student has raised their hand


raised_hands_queue = []
raised_hands_queue_lock = threading.Lock() #lock it because it is a shared resource

non_raised_hands_queue = [x for x in range(1,51)]
non_raised_hands_queue_lock = threading.Lock()

def student(id:int, raised_hands_queue:list, 
            raised_hands_queue_lock:threading.Lock, non_raised_hands_queue: list, 
            non_raised_hands_queue_lock:threading.Lock):
    while True:
        with raised_hands_queue_lock, non_raised_hands_queue_lock:
            if id not in raised_hands_queue and id not in non_raised_hands_queue: #people who have already participated
                break

        if random.randint(1,10) > 1:
            time.sleep(1)
            continue

        with raised_hands_queue_lock:
            if id in raised_hands_queue:
                raised_hands_queue.remove(id)
                with non_raised_hands_queue_lock:
                    non_raised_hands_queue.append(id)
                print(f"Student {id} lowered hand")
                continue

        non_raised_hands_queue_lock.acquire()
        if id in non_raised_hands_queue:
            non_raised_hands_queue.remove(id)
            raised_hands_queue_lock.acquire()
            raised_hands_queue.append(id)
            raised_hands_queue_lock.release()
            non_raised_hands_queue_lock.release()
            print(f"Student {id} raised hand")
            continue
        non_raised_hands_queue_lock.release()

def teacher(id:int, raised_hands_queue:list, 
            raised_hands_queue_lock:threading.Lock, non_raised_hands_queue: list, 
            non_raised_hands_queue_lock:threading.Lock):
    while True:
        student = None
        with raised_hands_queue_lock,non_raised_hands_queue_lock:
            if len(raised_hands_queue) + len(non_raised_hands_queue) == 0:
                print(f"Teacherr {id}: all students have presented")
                break
        with raised_hands_queue_lock:
            if len(raised_hands_queue) > 0:
                student= raised_hands_queue.pop(0)
        
        if student is None:
            with non_raised_hands_queue_lock:
                if len(non_raised_hands_queue) > 0:
                    student = non_raised_hands_queue.pop(0)

        if student is None:
            continue

        print(f"Student {student} is presenting with professor {id}")
        time.sleep(3)


with ThreadPoolExecutor(max_workers=52) as executor:
    for id in range(1,51):
        executor.submit(student, id, raised_hands_queue,raised_hands_queue_lock,non_raised_hands_queue,non_raised_hands_queue_lock)
    for id in range(1,3):
        executor.submit(teacher, id, raised_hands_queue,raised_hands_queue_lock,non_raised_hands_queue,non_raised_hands_queue_lock)












