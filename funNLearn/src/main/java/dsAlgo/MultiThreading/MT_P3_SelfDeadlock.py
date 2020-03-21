"""
    tag: thread, parallel

    Since in python a lock acquire call does not send the current thread details, 
    a thread can lock itself. Rlock removes this problem. 

"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class MTSelfDeadLock:
    def __init__(self):
        self.lock = Lock()

    def self_lock(self):
        print("acquired lock")
        self.lock.acquire()
        print("trying to self lock")
        self.lock.acquire()
        print("I am done processing")
        self.lock.release()

    def test_self_lock(self):
        my_thread = Thread(target=self.self_lock())
        my_thread.start()
        my_thread.join()


def run_tests():
    MTSelfDeadLock().test_self_lock()


run_tests()
