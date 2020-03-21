"""
    tag: thread, parallel
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_SameTime:
    def __init__(self):
        self.g = 0

    def add_one(self):
        time.sleep(3)
        print("add_one")
        self.g += 1

    def add_two(self):
        time.sleep(1)
        print("add_two")
        self.g += 2

    def test(self):
        thread_list = []
        for x in range(5):
            thread_list.append(Thread(target=self.add_one, name="t{}".format(x)))
            thread_list.append(Thread(target=self.add_two, name="t{}".format(x)))
            thread_list[-1].start()
            thread_list[-2].start()

        for t in thread_list:
            t.join()
        print("waiting for threads to complete!!!")

        print("Done! g: {}".format(self.g))


def run_tests():
    Multithreads_SameTime().test()


run_tests()
