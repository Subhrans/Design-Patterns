from threading import Thread, Lock, current_thread
from time import sleep


class TicketBooking:
    def __init__(self, total_ticket):
        self.total_ticket = total_ticket
        self.l = Lock()

    def book(self, need_ticket):
        self.l.acquire(blocking=True)
        print("available ticket ", self.total_ticket)
        if self.total_ticket !=0:
            sleep(3)
            name = current_thread().name
            print(f"ticket sold to {name}")
            self.total_ticket -= need_ticket
        else:
            print("All ticket sold")
        self.l.release()


a1 = TicketBooking(1)
t1 = Thread(target=a1.book, args=(1,),name="Subh")
t2 = Thread(target=a1.book, args=(1,),name="Sayan")

t1.start()
t2.start()