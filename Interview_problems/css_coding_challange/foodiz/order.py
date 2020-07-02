import logging
from datetime import datetime

logger = logging.getLogger("foodiz")


class OrderFactory:
    """
        Factory to provide order objects
    """

    def __init__(self, order_json):
        self.__orders_db_json = order_json
        self.__curr_order_indx = 0
        logger.info("Initialized")

    def get_next(self):
        """
            returns a new order object from the factory
            return None when empty
        """
        curr_order = None
        if self.__curr_order_indx < len(self.__orders_db_json):
            # COJ : current order json
            COJ = self.__orders_db_json[self.__curr_order_indx]
            curr_order = Order(
                COJ["id"], COJ["name"], COJ["temp"], COJ["shelfLife"], COJ["decayRate"]
            )
            self.__curr_order_indx += 1

        return curr_order


class Order:
    def __init__(self, id, name, temp, shelf_life, decay_rate):
        """
            defines an order object
        """
        self.id = id
        self.name = name
        self.temp = temp
        self.shelf_life = shelf_life
        self.decay_rate = decay_rate

        self.__cooked_time = None
        self.shelf = None

    def __eq__(self, to_order):
        return to_order.id == self.id

    def __str__(self):
        return str(self.id)

    def set_cooked(self):
        """
            sets the cooked ready time of the order to now. 
        """
        self.__cooked_time = datetime.now()

    def get_age(self):
        """
            return the age of order.
            time in seconds between food was cooked and now
        """
        return (datetime.now() - self.__cooked_time).total_seconds()

    def get_value(self):
        """
            Calculated based on the formula:
            value = (shelfLife - decayRate * orderAge * shelfDecayModifier) / shelfLife

            shelfDecayModifier is the decayModifier of the shelf it was kept on 
        """
        return (
            self.shelf_life
            - (self.decay_rate * self.get_age() * self.shelf.decay_modifier)
        ) / self.shelf_life
