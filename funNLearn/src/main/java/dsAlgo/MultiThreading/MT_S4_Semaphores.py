"""
    tag: thread, parallel

    Semaphores are simply advanced counters. 
    acquire() call to a semaphore will block only after a number of 
    threads have acquire()ed it. The associated counter decreases per 
    acquire() call, and increases per release() call. A ValueError 
    will occur if release() calls try to increment the counter beyond 
    its assigned maximum value (which is the number of threads that 
    can acquire() the semaphore before blocking occurs).
"""

from threading import Lock, Thread, RLock, BoundedSemaphore, Event, Condition, Barrier
import time, random


class Multithreads_Semaphores:
    def __init__(self, mc=5):
        self.max_connections = mc
        self.pool_sema = BoundedSemaphore(value=self.max_connections)
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

    def test_sema(self):
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


def run_tests():
    Multithreads_Semaphores(3).test_sema()


run_tests()
