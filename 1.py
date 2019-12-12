# Executing several tasks simultaneously is called multithreading

#2 types
#1-Process based multi tasking(at OS level)-
# Executing several tasks simultaneously where each task is a separate independent process.
#2. Thread based multi tasking(at program level)-
#Executing several tasks simultaneously,wehere each task is a seprate independent part of same programa,
# and each independent part is called a thread.
#advantage- Reduce execution time and increase performance

# Thread-1.Independent part of program 2. it is a task or action 3. an independent flow of execution


import time
from threading import *
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            time.sleep(2)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            time.sleep(2)


t1=Hello()
t2=Hi()
t1.start()
time.sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")