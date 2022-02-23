from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class RaceCondition:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

    def go(self):
        for i in range(1000000):
            self.increment()

    def test(self):
        # Run two threads that increment the counter:
        t1, t2 = Thread(target=self.go), Thread(target=self.go)
        t1.start()
        t2.start()
        t1.join()
        t2.join()

        # prints a number < 2,000,000 as t1 and t2 are racing to get value and incrementing it
        print(self.value)


class DeadLock:
    def __init__(self):
        self.phone_a = Lock()
        self.phone_b = Lock()

    def call_B(self):
        self.phone_a.acquire()  # picked up the receiver
        time.sleep(3)
        print("Friend A Dialing to call Friend B")
        self.phone_b.acquire()
        print("Friend A has called friend B")
        self.phone_b.release()
        self.phone_a.release()

    def call_A(self):
        self.phone_b.acquire()  # picked up the receiver
        time.sleep(3)
        print("Friend B Dialing to call Friend A")
        self.phone_a.acquire()
        print("Friend B has called friend A")
        self.phone_a.release()
        self.phone_b.release()

    def test(self):
        friendA = Thread(target=self.call_B)
        friendB = Thread(target=self.call_A)

        print("Both friends calling simultaneously")
        friendA.start()
        friendB.start()

        friendA.join()
        friendB.join()


class DeadLockSelf:
    def __init__(self):
        self.lock = Lock()

    def self_lock(self):
        self.lock.acquire()
        self.lock.acquire()    # will self lock here
        print("I am done processing")
        self.lock.release()

    def test(self):
        my_thread = Thread(target=self.self_lock())
        my_thread.start()
        my_thread.join()


class ThreadAware_RLock:
    # rlocks are thread aware and doesn't block when a thread is tryint to re-enter the lock. 
    # R-Lock = re-entrant lock.
    # Great for usage in recursion.
    def __init__(self):
        self.g = 0
        self.lock = Lock()
        self.rlock = RLock()

    def increment(self):
        self.rlock.acquire()
        self.g += 1
        self.rlock.acquire()
        self.g += 1
        self.rlock.release()

    def test(self):
        thread = Thread(target=self.increment)
        r_thread.start()
        r_thread.join()
        print("RLock thread completed")


class Multithreads_Lock:
    def __init__(self):
        self.g = 0
        self.lock = Lock()

    def add_one(self):
        self.lock.acquire()
        time.sleep(3)
        self.g += 1
        self.lock.release()

    def add_two(self):
        self.lock.acquire()
        time.sleep(1)
        self.g += 2
        self.lock.release()

    def test(self):
        thread_list = []
        for x in range(5):
            thread_list.append(Thread(target=self.add_one, name="t{}".format(x)))
            thread_list.append(Thread(target=self.add_two, name="t{}".format(x)))
            thread_list[-1].start()
            thread_list[-2].start()

        for t in thread_list:
            t.join()
        print("Done! g: {}".format(self.g))


"""
    Semaphores = advanced counters. 
    acquire(): increases the counter and block only after a number of threads have acquired it. 
    release(): reduce the counter
    maximum value: number of threads that can acquire()
"""
class SemaphoreThreadCounts:
    def __init__(self, max_connections=5):
        self.pool_sema = BoundedSemaphore(value=max_connections)
        self.db_connections = 0

    def exec_db_query(self, query="SELECT * from employee"):
        self.pool_sema.acquire()
        self.db_connections += 1
        print("DB ->", end="")  # conn = connectdb()
        print("Exec Query ->")
        time.sleep(1)
        print("close")  #  conn.close()
        self.db_connections -= 1
        self.pool_sema.release()

    def num_of_db_connections(self):
        while self.db_connections > 0:
            print(self.db_connections)
            time.sleep(1)

    def test(self):
        threads = []
        for _ in range(10):
            threads.append(Thread(target=self.exec_db_query))

        for t in threads:
            t.start()

        nt = Thread(target=self.num_of_db_connections)
        nt.start()

        for t in threads:
            t.join()

        nt.join()

# RaceCondition().test()
# DeadLock().test()
# DeadLockSelf().test()
# ThreadAware_RLock().test()
Multithreads_Lock().test()
SemaphoreThreadCounts().test()