#You are tasked with simulating a multi-threaded banking system where several users perform deposits and withdrawals on a shared bank account.
#The goal is to ensure data consistency under concurrent access.
#A single bank account starts with a balance of 1000€.
#3 depositor threads — each will deposit random amounts (between 50€ and 200€) a total of 10 times.
#3 withdrawal threads — each will withdraw random amounts (between 20€ and 150€) a total of 10 times.

import random
import time
import threading

balance = 1000
balance_lock = threading.Lock()

def deposit(name):
    global balance
    for i in range(10):
        amount = random.randint(49,109)
        time.sleep(random.random())

        with balance_lock:
            balance += amount
            print(f"Depositor {name} deposited {amount}€. Balance = {amount}€")


def withdraw(name):
    global balance
    for i in range(10):
        amount = random.randint(19,149)
        time.sleep(random.random())
        
        with balance_lock:
            if balance >= amount:
                balance = balance - amount

                print(f"Depositor {name} withdrew {amount}€. Balance = {balance}€")
            
            else:
                print(f"Withdrawer {name} waiting, insufficient funds (Balance = {balance}, requested = {amount})")


deposited = []
withdrawn = []

for x in range (3):
    t = threading.Thread(target = deposit, args=(x+1,))
    t.start()
    deposited.append(t)

for x in range (3):
    t = threading.Thread(target = withdraw, args=(x+1,))
    t.start()
    withdrawn.append(t)



for t in deposited + withdrawn : #the "+" combines them into 1 list
    t.join              #waits until thread t has finished running

print(f"\n All transactions complete. Final balance = {balance}€")











