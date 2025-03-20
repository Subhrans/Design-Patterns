from threading import Thread, Lock
import time

class Hotel:
    def __init__(self, task_name):
        self.task_name = task_name
        self.l = Lock()

    def food(self):
        self.l.acquire()
        for i in range(1, 6):
            time.sleep(0.1)  # Introduce a slight delay
            print(self.task_name, i)
        self.l.release()

h1 = Hotel("Take order from Table: ")
h2 = Hotel("Serve order to Table: ")

t1 = Thread(target=h1.food)
t2 = Thread(target=h2.food)

t1.start()
t2.start()
