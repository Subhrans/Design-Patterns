from threading import Thread, Event
from time import sleep


def light_switch():
    e1.set()
    print("Green light On")
    sleep(5)
    print("Red light on")
    e1.clear()

def traffic():
    e1.wait()
    while e1.is_set():
        print("You can go")
        sleep(1)
    print("Programme Done")
e1 = Event()

t1 = Thread(target=light_switch, name="light-switch-t1")
t2 = Thread(target=traffic, name="traffic-t2")
t1.start()
t2.start()

