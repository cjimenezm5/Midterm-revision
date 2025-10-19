#We have a class with 50 students and two teachers. Students will randomly decide to
#raise their hand and teachers will call them and they will give a presentation of 5
#seconds. A student may decide to lower their hand but the teacher will call a person
#they haven’t called if no student has raised their hand




#need: queues for kids who have and haven't raised their hands
#need: queues for professors, if both kid queues are empty, professor is done.
#need: if queue is not empty, checks queues (locks and unlocks the queues)


import time
import random
from concurrent.futures import ThreadPoolExecutor
import threading
import queue


NUM_STUDENTS = 50
NUM_TEACHERS = 2

raised_queue = queue.Queue()        # students who raised hand
not_raised_queue = queue.Queue()    # students not raising hand

#all students initially not raising their hands
for i in range(1, NUM_STUDENTS + 1):
    not_raised_queue.put(i)

print_lock = threading.Lock()

def student(student_id):
    
    while True:
        time.sleep(random.uniform(1, 3))  #wait before deciding
       
        action = random.choice(["raise", "lower"])  #decide to raise or lower hand randomly

        if action == "raise":
            if student_id in list(not_raised_queue.queue):       #move from not_raised to raised (if not already raised)
                not_raised_queue.queue.remove(student_id)
                raised_queue.put(student_id)
                with print_lock:
                    print(f"Student {student_id} raised hand ")

        else:                                               # lowers hand
            if student_id in list(raised_queue.queue):
                raised_queue.queue.remove(student_id)
                not_raised_queue.put(student_id)
                with print_lock:
                    print(f"Student {student_id} lowered hand ")

def teacher(teacher_id):
    while True:
        try:            #first students with raisedd hands
            student_id = raised_queue.get_nowait()
        except queue.Empty:
            try:                #if no raised hand, call someone not called
                student_id = not_raised_queue.get_nowait()
            except queue.Empty:
                with print_lock:
                    print(f"Teacher {teacher_id} is done. No students left.")
                break

        with print_lock:
            print(f"Teacher {teacher_id} calls Student {student_id} ")

       
        time.sleep(5)  # student presents for 5 seconds

        with print_lock:
            print(f"Student {student_id} finished presenting ")

        # After presenting, student is "done" (not re-added to any queue)

# Run simulation
with ThreadPoolExecutor(max_workers=NUM_STUDENTS + NUM_TEACHERS) as executor:
    # Launch students
    for sid in range(1, NUM_STUDENTS + 1):
        executor.submit(student, sid)

    # Launch teachers
    for tid in range(1, NUM_TEACHERS + 1):
        executor.submit(teacher, tid)
