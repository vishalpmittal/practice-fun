import logging
import json
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings
from utils import json_util
from threading import Thread
from foodiz.kitchen import Kitchen
from foodiz.order import OrderFactory

logger = logging.getLogger("foodiz")


class Command(BaseCommand):
    """
        custom django management command
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "-of",
            "--order_file",
            default=settings.DEFAULT_ORDER_FILE,
            type=str,
            help="define custom orders.json file for simulator",
        )
        parser.add_argument(
            "-or",
            "--order_rate",
            default=settings.DEFAULT_ORDER_RATE,
            type=int,
            help="Number of orders to accept per seconds, defaults to {} orders/sec".format(
                settings.DEFAULT_ORDER_RATE
            ),
        )

    def handle(self, *args, **kwargs):
        """
            management command handler
        """
        order_file = kwargs.get("order_file", None)
        order_rate = kwargs.get("order_rate", None)
        logger.info(
            'order_file: "{}" and order_rate: {} orders per secs'.format(
                order_file, order_rate
            )
        )

        # read the orders json file and initialize order factory
        orders_json = json_util.read_json(order_file)
        op = OrderFactory(orders_json)

        # initialize kitchen
        kc = Kitchen(order_wait=1 / order_rate)
        order_receive_thread = Thread(target=kc.receive_orders, args=[op])

        logger.info("Kitchen ready to receive orders")

        order_receive_thread.start()
        order_receive_thread.join()

        # wait for all the courier to dispatch remaining orders on shelf
        for t in kc.dispatched_courier_threads:
            t.join()

        logger.info("Simulation Complete!!!")
