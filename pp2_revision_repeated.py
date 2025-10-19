#We have a class with 50 students and two teachers. Students will randomly decide to
#raise their hand and teachers will call them and they will give a presentation of 5
#seconds. A student may decide to lower their hand but the teacher will call a person
#they haven’t called if no student has raised their hand

import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor



raised = []
raised_lock = threading.Lock()

non_raised = [x for x in range(1,51)]
non_raised_lock = threading.Lock()

def students(id: int, raised:list, non_raised:list, raised_lock: threading.Lock, non_raised_lock: threading.Lock):
    while True:

        with raised_lock, non_raised_lock:
            if id not in raised and id not in non_raised:
                break

        if random.randint(1,10) > 1:
            time.sleep(1)
            continue

        with raised_lock:   
            if id in raised:
                raised.remove(id)
                with non_raised_lock:
                    non_raised.append(id)
                print(f"Student {id} has lowered their hand")
                continue

        non_raised_lock.acquire()
        if id in non_raised:
            non_raised.remove(id)
            raised_lock.acquire()
            raised.append(id)
            raised_lock.release()
            non_raised_lock.release()
            print(f"Student {id} has raised their hand")
            continue
        non_raised_lock.release()


def teachers (id, raised: list, non_raised:list, raised_lock: threading.Lock, non_raised_lock: threading.Lock):

    while True:
        student = None

        with raised_lock, non_raised_lock:
            if len(raised) + len(non_raised) == 0:
                print("all students have presented")
                break
        
        with raised_lock:
            if len(raised)>0:
                student = raised.pop(0)
        
        if student is None:
            with raised_lock:
                if len(non_raised) > 0:
                    student = non_raised.pop(0)
                    
            
        if student is None:
            continue

        print(f"Teacher {id}: student {student} is presenting")
        time.sleep(3)

    print("All students have presented")


with ThreadPoolExecutor(max_workers = 52) as executor:
    for i in range(1, 51):
        executor.submit(students, i, raised, non_raised, raised_lock, non_raised_lock)
    for i in range(1,3):
        executor. submit(teachers, i, raised, non_raised, raised_lock, non_raised_lock)



























