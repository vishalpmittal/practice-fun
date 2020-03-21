"""
    tag: thread, parallel
"""

from queue import Queue
from threading import Lock, Condition, Event


class InitializationException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class QueueCapacityException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NoneObjectException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class MultiPutBlockingBoundedQueue_condition(object):
    def __init__(self):
        self.__queue__ = None
        self.__capacity__ = None
        self.__put_lock = Lock()
        self.__full_cond = Condition()

    def init(self, capacity):
        if self.__queue__:
            raise InitializationException()

        if capacity <= 0:
            raise QueueCapacityException()
        self.__queue__ = Queue()
        self.__capacity__ = capacity

    def get(self) -> object:
        obj = None
        self.__full_cond.acquire()
        if self.__queue__:
            obj = self.__queue__.get()
            self.__full_cond.notify_all()
        self.__full_cond.release()
        return obj

    def put(self, obj: object):
        if not self.__queue__:
            raise InitializationException()

        if not obj:
            raise NoneObjectException()

        self.__put_lock.acquire()
        self.__wait_or_put(obj)
        self.__put_lock.release()

    def multi_put(self, list_of_obj: List[object]):
        if not self.__queue__:
            raise InitializationException()
        if not list_of_obj:
            raise NoneObjectException()

        self.__put_lock.acquire()
        for obj in list_of_obj:
            self.__wait_or_put(obj)
        self.__put_lock.release()

    def __wait_or_put(self, obj):
        self.__full_cond.acquire()
        if len(self.__queue__) >= self.__capacity__:
            self.__full_cond.wait()
        self.__queue__.put(obj)
        self.__full_cond.release()


class MultiPutBlockingBoundedQueue_Event(object):
    def __init__(self):
        self.__queue__ = None
        self.__capacity__ = None
        self.__put_lock = Lock()
        self.__event = Event()

    def init(self, capacity):
        if self.__queue__:
            raise InitializationException()

        if capacity <= 0:
            raise QueueCapacityException()
        self.__queue__ = Queue()
        self.__capacity__ = capacity

    def get(self) -> object:
        obj = None
        if self.__queue__:
            obj = self.__queue__.get()
            self.__event.set()
        return obj

    def put(self, obj: object):
        if not self.__queue__:
            raise InitializationException()

        if not obj:
            raise NoneObjectException()

        self.__put_lock.acquire()
        self.__wait_or_put(obj)
        self.__put_lock.release()

    def multi_put(self, list_of_obj: List[object]):
        if not self.__queue__:
            raise InitializationException()
        if not list_of_obj:
            raise NoneObjectException()

        self.__put_lock.acquire()
        for obj in list_of_obj:
            self.__wait_or_put(obj)
        self.__put_lock.release()

    def __wait_or_put(self, obj):
        self.__full_cond.acquire()
        if len(self.__queue__) >= self.__capacity__:
            self.__event.wait()
        self.__queue__.put(obj)
        self.__event.clear()
        self.__full_cond.release()

