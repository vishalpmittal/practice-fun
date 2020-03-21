"""
    tag: thread, parallel

    A Condition object is simply a more advanced version of the Event object. 
    It too acts as a communicator between threads and can be used to notify() 
    other threads about a change in the state of the program. For example, it 
    can be used to signal the availability of a resource for consumption. 
    Other threads must also acquire() the condition (and thus its related lock) 
    before wait()ing for the condition to be satisfied. Also, a thread should 
    release() a Condition once it has completed the related actions, so that other 
    threads can acquire the condition for their purposes.
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_Conditions:
    def __init__(self):
        self.condition = Condition()
        self.box = []

    def producer(self, nitems):
        for i in range(nitems):
            time.sleep(random.randrange(2, 5))  # Sleeps for some time.
            self.condition.acquire()
            print('producer acquired condition')
            num = random.randint(1, 10)
            self.box.append(num)  # Puts an item into box for consumption.
            self.condition.notify()  # Notifies the consumer about the availability.
            print('producer noitifying condition')
            print("Produced:", num)
            self.condition.release()

    def consumer(self, nitems):
        for i in range(nitems):
            self.condition.acquire()
            print('consumer acquired condition')
            print('consumer might wait now')
            self.condition.wait()  # Blocks until an item is available for consumption.
            print("%s: Acquired: %s" % (time.ctime(), self.box.pop()))
            print('consumer releasing condition')
            self.condition.release()

    def test_conditions(self):
        threads = []
        nloops = random.randrange(3, 6)
        for func in [self.producer, self.consumer]:
            threads.append(Thread(target=func, args=[nloops]))
            threads[-1].start()  # Starts the thread.
        for thread in threads:
            thread.join()
        print("All done.")


def run_tests():
    print("Multithreads_Conditions")
    Multithreads_Conditions().test_conditions()


run_tests()
