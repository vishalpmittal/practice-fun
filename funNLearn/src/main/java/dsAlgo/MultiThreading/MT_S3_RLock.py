"""
    tag: thread, parallel
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_RLock:
    def __init__(self):
        self.g = 0
        self.lock = Lock()
        self.rlock = RLock()

    def increment_Lock(self):
        self.lock.acquire()
        self.g += 1
        # This will block the execution as thread t1 is already holding it.
        # but since with regular locks thread names are not specified, even
        # though t1 tries to acquire another lock around the same object, t1
        # will block itself.
        self.lock.acquire()
        self.g += 1
        self.lock.release()

    def increment_RLock(self):
        self.rlock.acquire()
        self.g += 1
        # rlocks are thread aware and doesn't block when a thread is tryint
        # to re-enter the lock. R-Lock = re-entrant lock.
        # Great for usage in recursion.
        self.rlock.acquire()
        self.g += 1
        self.rlock.release()

    def test(self):
        r_thread = Thread(target=self.increment_RLock)
        thread = Thread(target=self.increment_Lock)

        r_thread.start()
        r_thread.join()
        print("RLock thread completed")

        thread.start()
        print("Lock thread should be self blocked, press control C")
        # here we will be blocked.
        thread.join()


def run_tests():
    Multithreads_RLock().test()


run_tests()
