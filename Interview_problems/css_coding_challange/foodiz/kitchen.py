import time
import logging
from django.conf import settings
from foodiz.shelve import Shelf, SHELVES
from foodiz.order import OrderFactory, Order
from foodiz.courier import Courier
from threading import Thread, Lock
from queue import Queue

logger = logging.getLogger("foodiz")


class Kitchen:
    def __init__(self, order_wait=1 / settings.DEFAULT_ORDER_RATE):
        self.order_wait = order_wait
        self.dispatched_courier_threads = []
        logger.info("Initialized, order_receive wait time: {}".format(self.order_wait))

    def cook_order(self, order: Order):
        """
            prints the cooking order message and also sets the cooked timestamp
            returns None
        """
        logger.info("cooking order: {}".format(order))
        order.set_cooked()

    def place_on_shelve(self, order: Order):
        """
        -  put the order on the shelve that maches temperature 
        -  if the shelve is full put it on overflow shelve 
        -  If the overflow shelf is full, an existing order of your choosing 
           on the overflow should be moved to an allowable shelf with room.
        -  If no such move is possible, a random order from the overflow shelf 
           should be discarded as waste (and will not be available for a 
           courier pickup).
        """
        temp_shelf = SHELVES.get_shelf(order.temp)
        overflow_shelf = SHELVES.get_overflow_shelf()
        placed = False

        # Each order should be placed on a shelf that matches the order’s temperature
        temp_shelf.lock_shelf()
        if temp_shelf.has_space():
            temp_shelf.add_order(order)
            placed = True
        temp_shelf.unlock_shelf()

        # If that shelf is full, an order can be placed on the overflow shelf
        if not placed:
            overflow_shelf.lock_shelf()
            if overflow_shelf.has_space():
                overflow_shelf.add_order(order)
                placed = True
            overflow_shelf.unlock_shelf()

        # If the overflow shelf is full, an existing order of your choosing
        # on the overflow should be moved to an allowable shelf with room
        if not placed:
            overflow_shelf.lock_shelf()
            if overflow_shelf.move_an_item():
                overflow_shelf.add_order(order)
                placed = True
            overflow_shelf.unlock_shelf()

        # If no such move is possible, a random order from the overflow shelf
        # should be discarded as waste (and will not be available for a courier pickup).
        if not placed:
            overflow_shelf.lock_shelf()
            overflow_shelf.discard_random_order()
            overflow_shelf.add_order(order)
            overflow_shelf.unlock_shelf()

    def dispatch_courier(self, order: Order):
        """
            creates a new courier, assign the order object to it. 
            starts the courier thread
        """
        courier = Courier(order)
        courier_thred = Thread(target=courier.pickup_and_deliver)
        self.dispatched_courier_threads.append(courier_thred)
        courier_thred.start()

    def receive_orders(self, op: OrderFactory):
        """
            receives an order
            cooks the order
            places the order on the shelf, and parallelly dispatches the courier
            wait for predefined time to receive another oder

            Return when no more orders from the order factory
        """
        order = op.get_next()
        while order:
            logger.info("receive order: {}".format(order))
            self.cook_order(order)

            place_on_shelve_thread = Thread(target=self.place_on_shelve, args=[order])
            place_on_shelve_thread.start()

            dispatch_courier_thread = Thread(target=self.dispatch_courier, args=[order])
            dispatch_courier_thread.start()

            logger.info(
                "\n{} {} {} {} {} {}".format(
                    "=" * 70,
                    SHELVES.get_shelf("hot"),
                    SHELVES.get_shelf("cold"),
                    SHELVES.get_shelf("frozen"),
                    SHELVES.get_shelf("overflow"),
                    "=" * 70,
                )
            )

            logger.info(
                "waiting for {} before receiving next order".format(self.order_wait)
            )
            time.sleep(self.order_wait)
            order = op.get_next()
