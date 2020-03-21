"""
    tag: thread, parallel

    Using old style receiver phones
    if both friends A and B pickup their receivers at the same time and try 
    to call each other there will be a deadlock. In the example below 
    Friend A has Phone1 and friend B has phone 2
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class MTDeadlocksPhoneCall:
    def __init__(self):
        self.phone1 = Lock()
        self.phone2 = Lock()

    def call_B(self):
        self.phone1.acquire()  # picked up the receiver
        time.sleep(3)
        print("Friend A Dialing to call Friend B")
        self.phone2.acquire()
        print("Friend A has called friend B")
        self.phone2.release()
        self.phone1.release()

    def call_A(self):
        self.phone2.acquire()  # picked up the receiver
        time.sleep(3)
        print("Friend B Dialing to call Friend A")
        self.phone1.acquire()
        print("Friend B has called friend A")
        self.phone1.release()
        self.phone2.release()

    def friends_calling_deadlock(self):
        friendA = Thread(target=self.call_B)
        friendB = Thread(target=self.call_A)

        print("Both friends calling simultaneously")
        friendA.start()
        friendB.start()

        friendA.join()
        friendB.join()


def run_tests():
    MTDeadlocksPhoneCall().friends_calling_deadlock()


run_tests()
