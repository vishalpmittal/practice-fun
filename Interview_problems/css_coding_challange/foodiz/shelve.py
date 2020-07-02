from foodiz.order import Order
from threading import Lock
import random
import logging
from django.conf import settings

logger = logging.getLogger("foodiz")


class Shelf:
    def __init__(self, temperature, name, capacity, decay_modifier=1):
        self.temperature = temperature
        self.name = name
        self.capacity = capacity
        self.decay_modifier = decay_modifier

        self.__order_dict = dict()
        self.__lock = Lock()

    def __len__(self):
        return len(self.__order_dict)

    def __str__(self):
        return "\n{} {} ({}) {} \nItems: {}".format(
            "-" * 30, self.name, len(self), "-" * 30, list(self.__order_dict.keys())
        )

    def has_space(self):
        return len(self.__order_dict) < self.capacity

    def lock_shelf(self):
        self.__lock.acquire()

    def unlock_shelf(self):
        self.__lock.release()

    def add_order(self, order: Order) -> bool:
        """
            add order to the current shelf
        """
        self.__order_dict[order.id] = order
        order.shelf = self
        logger.info(": {}, added order: {}".format(self.name, order))

    def remove_order(self, order: Order):
        """
            removes an order from the shelf if found
            returns:
        """
        if order.id in self.__order_dict:
            del self.__order_dict[order.id]
            order.shelf = None
            logger.info(": {}, removed order: {}".format(self.name, order))

    def move_an_item(self):
        """
            find an item that can be moved to it's temperature shelf
            from overflow shelf. move the item and return true if a move 
            is made, or else return False. 

            This function is only applicable for overflow shelf
            for others it just returns False without moving
        """
        if self.temperature != "overflow":
            return False

        for order_id, order in self.__order_dict.items():
            # ots: order temperature shelf
            ots = SHELVES.get_shelf(order.temp)
            moved = False

            ots.lock_shelf()
            if ots.has_space():
                self.remove_order(order)
                ots.add_order(order)
                moved = True
            ots.unlock_shelf()

            if moved:
                logger.info(
                    ": {} moved order: {} to shelf: {}".format(
                        self.name, order.id, order.shelf.name
                    )
                )
                return True
        return False

    def discard_random_order(self):
        """
            Discards a random order from the shelf
            This function is only applicable for overflow shelf
            for others it just returns without discarding
        """
        if self.temperature != "overflow" or len(self.__order_dict) == 0:
            return

        ramdom_order_id = random.choice(list(self.__order_dict.keys()))
        random_order = self.__order_dict[ramdom_order_id]
        self.remove_order(random_order)
        logger.info(":{} Discard random order: {}".format(self.name, random_order))


class SHELVES:
    """
        Enum like class containing all the shelves
    """

    shelves = {
        s[0]: Shelf(s[0], s[1], int(s[2]), int(s[3])) for s in settings.SHELVES_LIST
    }

    @staticmethod
    def get_shelf(temperature: str):
        return SHELVES.shelves.get(temperature, None)

    @staticmethod
    def get_overflow_shelf():
        return SHELVES.shelves.get("overflow")
