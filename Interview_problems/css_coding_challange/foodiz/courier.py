import time
import logging
import random
from foodiz.shelve import Shelf
from foodiz.order import Order
from django.conf import settings

logger = logging.getLogger("foodiz")


class Courier:
    def __init__(self, order: Order):
        self.order = order
        logger.info("initialized for order: {}".format(order))

    def pickup_and_deliver(self):
        """
            picks up the after a random wait between 2-6 seconds
            prints appropriate messages for :
                -  if the order is not found anymore and was trashed earlier
                -  if the order is delivered
                -  if the order not good anymore
        """
        pickup_time = random.randrange(
            settings.COURIER_PICKUP_RANGE[0], settings.COURIER_PICKUP_RANGE[1]
        )
        logger.info(
            "on the way in {} secs, to pick up order: {}".format(
                pickup_time, self.order
            )
        )
        time.sleep(pickup_time)

        ord_shelf = self.order.shelf
        ord_value = None
        ord_action = "Order Not Found!!!"
        if ord_shelf:
            ord_shelf.lock_shelf()
            ord_value = self.order.get_value()
            ord_shelf.remove_order(self.order)
            ord_shelf.unlock_shelf()
            if ord_value <= 0:
                ord_action = "trashed wasted order"
            else:
                ord_action = "delivered order"

        logger.info(
            "{} : {}, order value: {}".format(ord_action, self.order, ord_value)
        )
