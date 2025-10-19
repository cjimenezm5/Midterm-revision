import logging
import threading
import time


def thread_function(name): #task run by thread = print start message, wait 5s and print finish message

    print(f"Thread {name}: starting", name)
    time.sleep(5)
    print(f"Thread {name}: finishing", name)

if __name__== "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format = format, level=logging.INFO, 
                        datefmt = "%H: %M: %S")
    print("Main : before creating thread")
    x= threading.Thread(target= thread_function, args= (1,)) #creates new thread and passes a tupple with 1 argument
    print("Main : before running thread")
    x.start()
    print("Main  : wait for the thread to finish")
    #x.join()
    print("Main : all done")












