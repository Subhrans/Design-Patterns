from threading import Thread, Condition
from time import sleep

list1 = []

def produce():
    cv.acquire()
    for i in range(1,5):
        list1.append(i)
        sleep(1)
        print("Item produce", i)

    # cv.notify()
    # cv.notify_all() # awake all threads
    cv.release()

def consume():
    cv.acquire()
    cv.wait(timeout=0)
    cv.release()
    # print("Printing ...")
    # sleep(2)
    print(list1)



cv = Condition()

t1 = Thread(target=produce, name="produce-t1")
t2 = Thread(target=consume, name="consume-t2")
# t3 = Thread(target=consume, name="consume-t3")

t1.start()
t2.start()
# t3.start()