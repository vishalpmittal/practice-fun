"""
    tag: thread, parallel

    reg_cb is an only api given to end user. 
    user uses the api to register a function/call back object. 
    all the call_back objects have a function call run()

    This run event should be ran for all the cb objects once an event_fired()
    has kicked. the envent_fired will be run only once, and any future registered
    cb objects should run immidiately.

                                        event_fired()
                                            |
                                            |
    ------------------------------------------------------------------->time
          |	              |              cb1.run()              |
          |               |              cb2.run()              |
       reg_cb(cb1)    reg_cb(cb2)                           reg_cb(cb3)
                                                             cb3.run()
    
    Considering run() takes a negligible execution time, design a system where 
    multiple users can call reg_cb and event_fired can happen at any instance 
    on the timeline. 
"""

from queue import Queue
from threading import Event, Thread, Lock

eq = Queue()  # eq = event queue
has_event_fired = False
lock = Lock()


def reg_cb(cb):
    if cb:
        eq.put(cb)

    # lock acquire outside eq.put() since even if multiple calls
    # should be able to put cb's in eq. But it's okay for the current 
    # run_regitstered_func to take care for whatever is in the queue
    # at that moment
    lock.acquire()
    if has_event_fired:
        run_registered_func()
    lock.release()


# this will be called only once
def event_fired():
    lock.acquire()
    has_event_fired = True
    run_registered_func()
    lock.release()


def run_registered_func():
    while len(eq) > 0:
        cfte = eq.get()  # cfte : current funtion to exec
        cfte.run()
