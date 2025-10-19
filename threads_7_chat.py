#There are 3 teachers who supervise students presenting projects.
#Each student raises their hand when ready.
#Teachers must always pick students who have raised their hands first, but if no one is ready, they wait.
#Simulate this classroom using two queues: raised and non-raised hands.

import time
import random
import threading
from concurrent.futures import ThreadPoolExecutor

# Shared resources
raised_hands = []
non_raised_hands = [x for x in range(1, 41)]

raised_hands_lock = threading.Lock()
non_raised_hands_lock = threading.Lock()


def students(id: int, raised_hands: list, non_raised_hands: list,
             raised_hands_lock: threading.Lock, non_raised_hands_lock: threading.Lock):
    """Students randomly raise or lower their hands."""
    while True:
        time.sleep(random.uniform(1, 3))  # random delay between decisions

        # Check if student already presented (removed from both lists)
        with raised_hands_lock, non_raised_hands_lock:
            if id not in raised_hands and id not in non_raised_hands:
                break

            # Random chance to raise or lower hand
            if random.randint(1, 10) < 3:
                if id in non_raised_hands:
                    non_raised_hands.remove(id)
                    raised_hands.append(id)
                    print(f"🙋 Student {id} has raised their hand")
                elif id in raised_hands:
                    raised_hands.remove(id)
                    non_raised_hands.append(id)
                    print(f"✋ Student {id} lowered their hand")


def teachers(id: int, raised_hands: list, non_raised_hands: list,
             raised_hands_lock: threading.Lock, non_raised_hands_lock: threading.Lock):
    """Teachers call on students to present, prioritizing raised hands."""
    while True:
        student = None

        # Check if everyone has presented
        with raised_hands_lock, non_raised_hands_lock:
            if len(raised_hands) + len(non_raised_hands) == 0:
                print(f"🧑‍🏫 Teacher {id}: all students have presented.")
                break

        # Pick a student from raised hands if available
        with raised_hands_lock:
            if len(raised_hands) > 0:
                student = raised_hands.pop(0)

        # If none are ready, pick from non-raised
        if student is None:
            with non_raised_hands_lock:
                if len(non_raised_hands) > 0:
                    student = non_raised_hands.pop(0)

        # If still no one, wait and retry
        if student is None:
            time.sleep(1)
            continue

        # Student presents
        print(f"🧑‍🏫 Teacher {id}: Student {student} is presenting...")
        time.sleep(random.uniform(3, 5))
        print(f"🎓 Student {student} finished presenting.")

        # Remove student completely (they are done)
        with raised_hands_lock, non_raised_hands_lock:
            if student in raised_hands:
                raised_hands.remove(student)
            if student in non_raised_hands:
                non_raised_hands.remove(student)


# Run the simulation
with ThreadPoolExecutor(max_workers=43) as executor:
    # 3 teachers
    for i in range(1, 4):
        executor.submit(teachers, i, raised_hands, non_raised_hands,
                        raised_hands_lock, non_raised_hands_lock)

    # 40 students
    for i in range(1, 41):
        executor.submit(students, i, raised_hands, non_raised_hands,
                        raised_hands_lock, non_raised_hands_lock)



















