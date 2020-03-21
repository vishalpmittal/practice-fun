"""
    tag: thread, parallel
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class MTRaceCondition:
    class Counter:
        def __init__(self):
            self.value = 0

        def increment(self):
            self.value += 1

    def test_race_condition(self):
        c = self.Counter()

        def go():
            for i in range(1000000):
                c.increment()

        # Run two threads that increment the counter:
        t1 = Thread(target=go)
        t1.start()
        t2 = Thread(target=go)
        t2.start()
        t1.join()
        t2.join()

        # should print 2,000,000 but prints lesser value
        # this is because of the race condition from two threads
        # trying to get to the counter object and incrementing it
        print(c.value)


def run_tests():
    MTRaceCondition().test_race_condition()


run_tests()
