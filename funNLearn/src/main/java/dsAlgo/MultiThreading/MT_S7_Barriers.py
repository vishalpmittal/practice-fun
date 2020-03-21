"""
    tag: thread, parallel

    A barrier is a simple synchronization primitive which can be used by different 
    threads to wait for each other. Each thread tries to pass a barrier by calling 
    the wait() method, which will block until all of threads have made that call. 
    As soon as that happens, the threads are released simultaneously.

    It's like ready,get set, go in a race. Just wait until all the players are ready. 
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_Barriers:
    def __init__(self):
        # 4 threads will need to pass this barrier to get released.
        self.num = 4
        self.b = Barrier(self.num)
        self.names = ["Harsh", "Lokesh", "George", "Iqbal"]

    def player(self):
        name = self.names.pop()
        time.sleep(random.randrange(2, 5))
        print("%s reached the barrier at: %s" % (name, time.ctime()))
        self.b.wait()

    def test_barrier(self):
        threads = []
        print("Race starts now…")
        for i in range(self.num):
            threads.append(Thread(target=self.player))
            threads[-1].start()
        for thread in threads:
            thread.join()
        print("Race over!")


def run_tests():
    Multithreads_Barriers().test_barrier()


run_tests()
