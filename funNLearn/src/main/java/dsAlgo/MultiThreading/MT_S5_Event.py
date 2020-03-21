"""
    tag: thread, parallel

    The Event synchronization primitive acts as a simple communicator between 
    threads. They are based on an internal flag which threads can set() or clear(). 
    Other threads can wait() for the internal flag to be set().
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_Event:
    def __init__(self):
        self.event = Event()

    def waiter(self, nloops):
        for i in range(nloops):
            print("%s. Waiting for the flag to be set." % (i + 1))
            self.event.wait()  # Blocks until the flag becomes true.
            print("Wait complete at:", time.ctime())
            self.event.clear()  # Resets the flag.
            print()

    def setter(self, nloops):
        for i in range(nloops):
            time.sleep(random.randrange(2, 5))  # Sleeps for some time.
            self.event.set()

    def test_event(self):
        threads = []
        nloops = random.randrange(3, 6)

        threads.append(Thread(target=self.waiter, args=[nloops]))
        threads[-1].start()
        threads.append(Thread(target=self.setter, args=[nloops]))
        threads[-1].start()

        for thread in threads:
            thread.join()

        print("All done.")


def run_tests():
    print("Multithreads Events")
    Multithreads_Event().test_event()


run_tests()
